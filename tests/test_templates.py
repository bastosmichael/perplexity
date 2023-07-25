from perplexity.templates import CHAT_PROMPT_TEMPLATE

def test_chat_prompt_template():
    assert isinstance(CHAT_PROMPT_TEMPLATE.messages, list)
