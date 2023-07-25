from typing import AsyncGenerator
import pytest
from unittest.mock import AsyncMock, patch
from perplexity.conversation_chain import StreamingConversationChain
from perplexity.templates import CHAT_PROMPT_TEMPLATE

@pytest.mark.asyncio
async def test_streaming_conversation_chain():
    openai_api_key = "fake_api_key"
    temperature = 0.5
    conversation_id = "conversation_1"
    message = "Hello, how are you?"

    # Create instance of StreamingConversationChain
    scc = StreamingConversationChain(openai_api_key, temperature)

    # Mock AsyncIteratorCallbackHandler, ChatOpenAI, ConversationBufferMemory, ConversationChain
    with patch('langchain.callbacks.AsyncIteratorCallbackHandler') as mock_aiter, \
         patch('langchain.chat_models.ChatOpenAI') as mock_chat, \
         patch('langchain.memory.ConversationBufferMemory') as mock_memory, \
         patch('langchain.chains.ConversationChain') as mock_chain:
        
        mock_aiter.return_value.aiter.return_value = AsyncMock()
        mock_chat.return_value = AsyncMock()
        mock_memory.return_value = AsyncMock()
        mock_chain.return_value.arun.return_value = AsyncMock()

        async_gen = scc.generate_response(conversation_id, message)

        # Expect to get generator object
        assert isinstance(async_gen, AsyncGenerator)

        response = await next(async_gen)
        
        # Assertions
        mock_chat.assert_called_once_with(callbacks=[mock_aiter.return_value],
                                          streaming=True,
                                          temperature=temperature,
                                          openai_api_key=openai_api_key)

        mock_memory.assert_called_once_with(return_messages=True)
        assert scc.memories[conversation_id] is not None

        mock_chain.assert_called_once_with(memory=mock_memory.return_value,
                                           prompt=CHAT_PROMPT_TEMPLATE,
                                           llm=mock_chat.return_value)

        mock_chain.return_value.arun.assert_called_once_with(input=message)

        # Check if token is returned from generator
        assert response is not None
