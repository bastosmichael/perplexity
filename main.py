import asyncio
from functools import lru_cache
from typing import AsyncGenerator

from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    """
    Settings class for this application.
    Utilizes the BaseSettings from pydantic for environment variables.
    """

    openai_api_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    """Function to get and cache settings.
    The settings are cached to avoid repeated disk I/O.
    """
    return Settings()


class StreamingConversationChain:
    """
    Class for handling streaming conversation chains.
    It creates and stores memory for each conversation,
    and generates responses using the ChatOpenAI model from LangChain.
    """

    def __init__(self, openai_api_key: str, temperature: float = 0.0):
        self.memories = {}
        self.openai_api_key = openai_api_key
        self.temperature = temperature

    async def generate_response(
        self, conversation_id: str, message: str
    ) -> AsyncGenerator[str, None]:
        """
        Asynchronous function to generate a response for a conversation.
        It creates a new conversation chain for each message and uses a
        callback handler to stream responses as they're generated.
        :param conversation_id: The ID of the conversation.
        :param message: The message from the user.
        """
        callback_handler = AsyncIteratorCallbackHandler()
        llm = ChatOpenAI(
            callbacks=[callback_handler],
            streaming=True,
            temperature=self.temperature,
            openai_api_key=self.openai_api_key,
        )

        memory = self.memories.get(conversation_id)
        if memory is None:
            memory = ConversationBufferMemory(return_messages=True)
            self.memories[conversation_id] = memory

        chain = ConversationChain(
            memory=memory,
            prompt=CHAT_PROMPT_TEMPLATE,
            llm=llm,
        )

        run = asyncio.create_task(chain.arun(input=message))

        async for token in callback_handler.aiter():
            yield token

        await run


class ChatRequest(BaseModel):
    """Request model for chat requests.
    Includes the conversation ID and the message from the user.
    """

    conversation_id: str
    message: str


CHAT_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "You're a AI that knows everything about code."
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

app = FastAPI(dependencies=[Depends(get_settings)])

streaming_conversation_chain = StreamingConversationChain(
    openai_api_key=get_settings().openai_api_key
)


@app.post("/chat", response_class=StreamingResponse)
async def generate_chat_response(data: ChatRequest):
    return StreamingResponse(
        streaming_conversation_chain.generate_response(
            data.conversation_id, data.message
        ),
        media_type="text/event-stream",
    )

@app.post("/chat", response_class=StreamingResponse)
async def chat(data: ChatRequest) -> StreamingResponse:
    return await generate_chat_response(data)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
