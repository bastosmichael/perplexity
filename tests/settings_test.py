from perplexity.settings import Settings, get_settings


def test_get_settings():
    settings = get_settings()
    assert isinstance(settings, Settings)
    assert hasattr(settings, "openai_api_key")
    assert hasattr(settings, "anthropic_api_key")
    assert hasattr(settings, "azure_openai_api_key")
    assert hasattr(settings, "fake_list_api_key")
    assert hasattr(settings, "google_palm_api_key")
    assert hasattr(settings, "human_input_api_key")
    assert hasattr(settings, "jina_api_key")
    assert hasattr(settings, "prompt_layer_openai_api_key")
    assert hasattr(settings, "vertex_ai_api_key")
