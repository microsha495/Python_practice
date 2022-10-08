class Matrix:
    def __init__(self, li):
        self.li = li

    def __str__(self):
        return '\n'.join('\t'.join(str(cell) for cell in row) for row in self.li)

    def __add__(self, other):
        res_li = []
        for i, row in enumerate(self.li):
            inner_li = []
            for j, cell in enumerate(self.li[i]):
                inner_li.append(self.li[i][j] + other.li[i][j])
            res_li.append(inner_li)
        return Matrix(res_li)


a = Matrix([[12, 2], [3, 4]])
b = Matrix([[4, 5], [5, 3]])
c = a + b
print(c)