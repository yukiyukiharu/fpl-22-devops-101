from app.nlp import normalize_text, tokenize, detect_language, basic_stats


def test_normalize_text():
    assert normalize_text("  HeLLo  ") == "hello"


def test_tokenize():
    assert tokenize("Hello, world!") == ["Hello", "world"]


def test_detect_language_ru():
    assert detect_language("Привет, мир") == "ru"


def test_detect_language_en():
    assert detect_language("Hello, world") == "en/other"


def test_basic_stats():
    text = "Привет, мир! Привет!"
    stats = basic_stats(text, top_n=2)
    assert stats["total_words"] == 3
    assert stats["unique_words"] == 2
    assert stats["language"] == "ru"
    assert stats["top_words"][0][0] == "привет"
