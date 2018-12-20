from string import ascii_uppercase as ALPHABET
from random import choice, randint


def create_random_name():
        return choice(ALPHABET) + choice(ALPHABET) + str(randint(0, 9)) +\
                str(randint(0, 9)) + str(randint(0, 9))


class Robot(object):
    names = set()

    def reset(self):
        new_name = create_random_name()
        while new_name in self.names:
            new_name = create_random_name()

        self.names.remove(self.name)
        self.name = new_name
        self.names.add(self.name)

    def __init__(self):
        self.name = create_random_name()
        while self.name in self.names:
            self.name = create_random_name()

        self.names.add(self.name)
