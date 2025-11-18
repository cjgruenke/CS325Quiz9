def count_words(text: str) -> int:
    if not text:
        return 0
    return len(text.split())

def count_chars(text: str) -> int:
    if text is None:
        return 0
    return len(text)

def count_sentences(text: str) -> int:
    if not text:
        return 0
    sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return len(sentences)

def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.splitlines())

def longest_word(text: str) -> str:
    if not text:
        return ""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
