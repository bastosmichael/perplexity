from perplexity.conversation_chain import StreamingConversationChain
from perplexity.settings import get_settings
from perplexity.models.model_classes import MODEL_CLASSES


def anthropic_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatAnthropic",
        api_key=get_settings().anthropic_api_key,
        temperature=0.5,
    )


def azure_chat_openai_conversation_chain():
    return StreamingConversationChain(
        model_type="AzureChatOpenAI",
        api_key=get_settings().azure_openai_api_key,
        temperature=0.5,
    )


def fake_list_chat_model_conversation_chain():
    return StreamingConversationChain(
        model_type="FakeListChatModel",
        api_key=get_settings().fake_list_api_key,
        temperature=0.5,
    )


def chat_google_palm_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatGooglePalm",
        api_key=get_settings().google_palm_api_key,
        temperature=0.5,
    )


def human_input_chat_model_conversation_chain():
    return StreamingConversationChain(
        model_type="HumanInputChatModel",
        api_key=get_settings().human_input_api_key,
        temperature=0.5,
    )


def jina_chat_conversation_chain():
    return StreamingConversationChain(
        model_type="JinaChat",
        api_key=get_settings().jina_api_key,
        temperature=0.5,
    )


def chat_openai_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatOpenAI",
        api_key=get_settings().openai_api_key,
        temperature=0.5,
    )


def prompt_layer_chat_openai_conversation_chain():
    return StreamingConversationChain(
        model_type="PromptLayerChatOpenAI",
        api_key=get_settings().prompt_layer_openai_api_key,
        temperature=0.5,
    )


def chat_vertex_ai_conversation_chain():
    return StreamingConversationChain(
        model_type="ChatVertexAI",
        api_key=get_settings().vertex_ai_api_key,
        temperature=0.5,
    )
