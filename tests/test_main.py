from fastapi.testclient import TestClient
from perplexity.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"conversation_id": "123", "message": "Hello, world!"})
    assert response.status_code == 200
