import string

from encoded_type import EncodedType

ALPHANUMERIC_CHARS = set(string.digits + string.ascii_uppercase + " $%*+-/.:")


def __isISO88591(s):
    try:
        s.encode("iso-8859-1")
        return True
    except UnicodeEncodeError:
        return False


def __isAlphanum(s):
    for c in s:
        if c not in ALPHANUMERIC_CHARS:
            return False
    return True


def __isKanji(s):
    try:
        s.encode("shift-jis")
        return True
    except UnicodeEncodeError:
        return False


def analyze(s):
    if s.isnumeric():
        return EncodedType.NUMERIC
    elif __isAlphanum(s):
        return EncodedType.ALPHANUMERIC
    elif __isISO88591(s):
        return EncodedType.BYTE
    elif __isKanji(s):
        return EncodedType.KANJI
    else:
        raise Exception("Encoding type not supported")
