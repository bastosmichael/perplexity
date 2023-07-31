from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from perplexity.models.chat_request import ChatRequest
from perplexity.dependencies import openai_conversation_chain, anthropic_conversation_chain

router = APIRouter()

@router.post("/openai", response_class=StreamingResponse)
async def generate_openai_chat_response(data: ChatRequest, chain=Depends(openai_conversation_chain)):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )

@router.post("/anthropic", response_class=StreamingResponse)
async def generate_anthropic_chat_response(data: ChatRequest, chain=Depends(anthropic_conversation_chain)):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )
