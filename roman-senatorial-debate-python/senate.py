import random


class Senator:
    def __init__(self, name: str):
        self.name = name


class Leaning:

    def __init__(self, senators: list[Senator], leanings: dict[Senator, int]):
        self.leaning = leanings
        self.senators = senators

    def generate_leaning(self):
        return {senator: random.randint(-1, 1) * 10 for senator in self.senators}


class Debate:
    def __init__(self, motion: str, senators: list[Senator]):
        self.motion = motion
        self.senators = senators
        self.initial_leanings = self.generate_leaning()

    def 

class Senate:
    def __init__(
        self,
        number_of_senators: int,
    ):
        self.number_of_senators = number_of_senators

    def add_senator(self, senator: Senator):
        self.senators.append(senator)

    def remove_senator(self, senator: Senator):
        self.senators.remove(senator)
