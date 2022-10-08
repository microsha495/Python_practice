from abc import abstractmethod
class Clothes:
    @abstractmethod
    def fabric_cons(self):
        pass
    def __add__(self, other):
        gen_cons = round((self.fabric_cons + other.fabric_cons), 2)
        return f'general consumption for clothes: {gen_cons}'


class Coat(Clothes):
    def __init__(self, v):
        self.v = v
    @property
    def fabric_cons(self):
        f_cons_coat = round((self.v / 6.5 + 0.5), 2)
        return f_cons_coat
    def __str__(self):
        return f'fabric consumption for coat: {self.fabric_cons}'

class Suite(Clothes):
    def __init__(self, h):
        self.h = h
    @property
    def fabric_cons(self):
        f_cons_suite = round((self.h * 2 + 0.3), 2)
        return f_cons_suite
    def __str__(self):
        return f'fabric consumption for suite: {self.fabric_cons}'

coat = Coat(46)
print(coat.fabric_cons)
print(coat)
suite = Suite(100)
print(coat + suite)