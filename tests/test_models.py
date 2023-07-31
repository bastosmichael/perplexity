from perplexity.models.chat_request import ChatRequest


def test_chat_request_model():
    data = {"conversation_id": "123", "message": "Hello, world!"}
    chat_request = ChatRequest(**data)

    assert chat_request.conversation_id == "123"
    assert chat_request.message == "Hello, world!"
