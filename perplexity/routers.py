from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from perplexity.models.chat_request import ChatRequest
from perplexity.dependencies import (
    anthropic_conversation_chain,
    azure_chat_openai_conversation_chain,
    fake_list_chat_model_conversation_chain,
    chat_google_palm_conversation_chain,
    human_input_chat_model_conversation_chain,
    jina_chat_conversation_chain,
    chat_openai_conversation_chain,
    prompt_layer_chat_openai_conversation_chain,
    chat_vertex_ai_conversation_chain,
)

router = APIRouter()


@router.post("/openai", response_class=StreamingResponse, tags=["Conversation Chains"])
async def generate_openai_chat_response(
    data: ChatRequest, chain=Depends(chat_openai_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/anthropic", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_anthropic_chat_response(
    data: ChatRequest, chain=Depends(anthropic_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post("/azure", response_class=StreamingResponse, tags=["Conversation Chains"])
async def generate_azure_chat_response(
    data: ChatRequest, chain=Depends(azure_chat_openai_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/fake_list", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_fake_list_chat_response(
    data: ChatRequest, chain=Depends(fake_list_chat_model_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/google_palm", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_google_palm_chat_response(
    data: ChatRequest, chain=Depends(chat_google_palm_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/human_input", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_human_input_chat_response(
    data: ChatRequest, chain=Depends(human_input_chat_model_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post("/jina", response_class=StreamingResponse, tags=["Conversation Chains"])
async def generate_jina_chat_response(
    data: ChatRequest, chain=Depends(jina_chat_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/prompt_layer", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_prompt_layer_chat_response(
    data: ChatRequest, chain=Depends(prompt_layer_chat_openai_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )


@router.post(
    "/vertex_ai", response_class=StreamingResponse, tags=["Conversation Chains"]
)
async def generate_vertex_ai_chat_response(
    data: ChatRequest, chain=Depends(chat_vertex_ai_conversation_chain)
):
    return StreamingResponse(
        chain.generate_response(data.conversation_id, data.message),
        media_type="text/event-stream",
    )
