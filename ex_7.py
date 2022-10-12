class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


c1 = ComplexNumber(2, 5)
c2 = ComplexNumber(7, -4)
print(f'c1 = {c1}\nc2 = {c2}')
print(c1 + c2)
print(c1 * c2)
