from perplexity.conversation_chain import StreamingConversationChain
from perplexity.settings import get_settings


def openai_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatOpenAI", api_key=get_settings().openai_api_key, temperature=0.5
    )


def anthropic_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatAnthropic",
        api_key=get_settings().anthropic_api_key,
        temperature=0.5,
    )
