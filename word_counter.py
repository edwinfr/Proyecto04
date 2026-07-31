import re


def count_words(text: str) -> int:
    words = re.findall(r"\b\w+\b", text.lower())
    return len(words)
