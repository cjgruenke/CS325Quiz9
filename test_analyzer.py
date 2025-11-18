import pytest
from analyzer import (
    count_words,
    count_chars,
    count_sentences,
    count_lines,
    longest_word
)
def test_basic_counts():
    text = "Hello world! This is a test."
    assert count_words(text) == 6
    assert count_chars(text) == len(text)
    assert count_sentences(text) == 2
    assert count_lines(text) == 1

def test_longest_word_and_empty():
    assert longest_word("hi hello supercalifragilisticexpialidocious") == "supercalifragilisticexpialidocious"
    assert count_words("") == 0
    assert count_sentences("") == 0
    assert longest_word("") == ""
