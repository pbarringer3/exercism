from re import search


def is_shouting(phrase):
    if search('[a-zA-Z]', phrase) and phrase == phrase.upper():
        return True
    return False


def is_question(phrase):
    if phrase[-1] == "?":
        return True
    return False


def hey(phrase):
    phrase = phrase.strip()
    if len(phrase) == 0:
        return "Fine. Be that way!"
    elif is_question(phrase):
        if is_shouting(phrase):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif is_shouting(phrase):
        return "Whoa, chill out!"
    return "Whatever."
