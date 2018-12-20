import re


def abbreviate(words):
    return "".join([word[0] for word in list(filter(lambda x: len(x) > 0,
                   re.split(' |-', words)))]).upper()
