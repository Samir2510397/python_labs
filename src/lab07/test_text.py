import pytest
from src.lib import normalize, tokenize, count_freq, top_n

##Параметризуем
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello  world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a","b","a","c","b","a"], {"a": 3, "b": 2, "c": 1}),
        (["bb","aa","bb","aa","cc"], {"aa": 2, "bb": 2, "cc": 1}),
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"a":3,"b":2,"c":1}, 2, [('a', 3), ('b', 2)]),
        ({"aa":2,"bb":2,"cc":1}, 2, [('aa', 2), ('bb', 2)]),
    ],
)
def test_top_n(source, n, expected):
    assert top_n(source, n) == expected