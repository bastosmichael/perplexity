from perplexity.settings import Settings, get_settings

def test_get_settings():
    settings = get_settings()
    assert isinstance(settings, Settings)
    assert hasattr(settings, 'openai_api_key')
