from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse
from perplexity.settings import get_settings
from perplexity.models import ChatRequest
from perplexity.conversation_chain import StreamingConversationChain

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


def main():
    import uvicorn

    uvicorn.run("perplexity.main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
