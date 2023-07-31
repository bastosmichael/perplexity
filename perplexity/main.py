from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse
from perplexity.settings import get_settings
from perplexity.models.chat_request import ChatRequest
from perplexity.conversation_chain import StreamingConversationChain

app = FastAPI(dependencies=[Depends(get_settings)])

openai_conversation_chain = StreamingConversationChain(
    model_type="ChatOpenAI", api_key=get_settings().openai_api_key, temperature=0.5
)

anthropic_conversation_chain = StreamingConversationChain(
    model_type="ChatAnthropic",
    api_key=get_settings().anthropic_api_key,
    temperature=0.5,
)


@app.post("/openai", response_class=StreamingResponse)
async def generate_openai_chat_response(data: ChatRequest):
    return StreamingResponse(
        openai_conversation_chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@app.post("/anthropic", response_class=StreamingResponse)
async def generate_anthropic_chat_response(data: ChatRequest):
    return StreamingResponse(
        anthropic_conversation_chain.generate_response(
            data.conversation_id, data.message
        ),
        media_type="text/event-stream",
    )


def main():
    import uvicorn

    uvicorn.run("perplexity.main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
