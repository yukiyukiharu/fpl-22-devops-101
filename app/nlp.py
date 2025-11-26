import re
from collections import Counter
from typing import List, Dict, Any


def normalize_text(text: str) -> str:
    '''Simple text normalizer'''
    return text.strip().lower()


def tokenize(text: str) -> List[str]:
    '''Simple text tokenizer'''
    return re.findall(r"\w+", text, flags=re.UNICODE)


def detect_language(text: str) -> str:
    '''
    Naive language detection:
    - if text contains cyrillic symbols → "ru"
    - if text does not contain cyrillic symbols → "en/other"
    '''
    if re.search(r"[А-Яа-яЁё]", text):
        return "ru"
    return "en/other"


def basic_stats(text: str, top_n: int = 3) -> Dict[str, Any]:
    '''
    Basic text stat:
    - general word count
    - unique word count
    - most frequent words N-number 
    - language
    '''
    normalized = normalize_text(text)
    tokens = tokenize(normalized)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    lang = detect_language(normalized)

    counter = Counter(tokens)
    top_words = counter.most_common(top_n)

    return {
        "normalized": normalized,
        "total_words": total_words,
        "unique_words": unique_words,
        "language": lang,
        "top_words": top_words,
    }
