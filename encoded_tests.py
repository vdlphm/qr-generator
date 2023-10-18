import pytest
from type_determinator import analyze
from encoded_type import EncodedType


def test_encoded_numeric():
    assert analyze("12345") == EncodedType.NUMERIC


def test_encoded_alphanumeric():
    assert analyze("123B334") == EncodedType.ALPHANUMERIC


def test_encoded_iso558951():
    assert analyze("123â") == EncodedType.BYTE


def test_encoded_kanji():
    assert analyze("プログラマ") == EncodedType.KANJI


def test_encoded_failed_iso558951_alike():
    with pytest.raises(Exception):
        analyze("Đâ")


def test_encode_failed_korean():
    with pytest.raises(Exception):
        analyze("ㅃ")
