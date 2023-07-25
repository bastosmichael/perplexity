from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Request model for chat requests.
    Includes the conversation ID and the message from the user.
    """

    conversation_id: str
    message: str
