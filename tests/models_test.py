import unittest
from perplexity.models.chat_request import ChatRequest
from perplexity.models.model_classes import MODEL_CLASSES
from langchain.chat_models import (
    ChatAnthropic,
    AzureChatOpenAI,
    FakeListChatModel,
    ChatGooglePalm,
    HumanInputChatModel,
    JinaChat,
    ChatOpenAI,
    PromptLayerChatOpenAI,
    ChatVertexAI,
)


def test_chat_request_model():
    data = {"conversation_id": "123", "message": "Hello, world!"}
    chat_request = ChatRequest(**data)

    assert chat_request.conversation_id == "123"
    assert chat_request.message == "Hello, world!"


class TestModelClasses(unittest.TestCase):
    def setUp(self):
        self.model_classes_keys = [
            "ChatAnthropic",
            "AzureChatOpenAI",
            "FakeListChatModel",
            "ChatGooglePalm",
            "HumanInputChatModel",
            "JinaChat",
            "ChatOpenAI",
            "PromptLayerChatOpenAI",
            "ChatVertexAI",
        ]
        self.expected_classes = [
            ChatAnthropic,
            AzureChatOpenAI,
            FakeListChatModel,
            ChatGooglePalm,
            HumanInputChatModel,
            JinaChat,
            ChatOpenAI,
            PromptLayerChatOpenAI,
            ChatVertexAI,
        ]
        self.expected_api_key_names = [
            "anthropic_api_key",
            "azure_openai_api_key",
            "fake_list_api_key",
            "google_palm_api_key",
            "human_input_api_key",
            "jina_api_key",
            "openai_api_key",
            "prompt_layer_openai_api_key",
            "vertex_ai_api_key",
        ]

    def test_model_classes(self):
        for i, key in enumerate(self.model_classes_keys):
            with self.subTest(i=i):
                self.assertIn(key, MODEL_CLASSES)
                self.assertEqual(MODEL_CLASSES[key]["class"], self.expected_classes[i])
                self.assertEqual(
                    MODEL_CLASSES[key]["api_key_name"], self.expected_api_key_names[i]
                )


if __name__ == "__main__":
    unittest.main()
