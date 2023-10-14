from encoded_type import EncodedType


def __isISO88591(s):
    try:
        s.encode("iso-8859-1")
        return True
    except UnicodeEncodeError:
        return False


def __isAlphanum(s):
    try:
        s.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


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
