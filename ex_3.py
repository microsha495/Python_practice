class Cell:
    def __init__(self, cell_unit):
        self.cell_unit = int(cell_unit)
    def __add__(self, other):
        return self.cell_unit + other.cell_unit
    def __sub__(self, other):
        if (self.cell_unit - other.cell_unit) >= 0:
            return self.cell_unit - other.cell_unit
        else:
            return f'the difference cannot be less than 0'
    def __mul__(self, other):
        return self.cell_unit * other.cell_unit
    def __truediv__(self, other):
        if self.cell_unit % other.cell_unit == 0:
            return round(self.cell_unit // other.cell_unit)
        else:
            return round(self.cell_unit // other.cell_unit) + 1
    def make_order(self):
        a = '*'
        cell_str = a * self.cell_unit
        print('\n'.join(cell_str[i:i + 5] for i in range(0, len(cell_str), 5)))

a = Cell(16)
b = Cell(5)
print(a + b)
print(a - b)
print(b - a)
print(a / b)
a.make_order()

