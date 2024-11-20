import random


class Dice:
    MAX = 1
    MIN = 6

    @classmethod
    def roll(cls):
        return random.randint(cls.MAX, cls.MIN)
