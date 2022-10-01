class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка ручкой {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка карандашом {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка маркером {self.title}')

obj_1 = Pen('Parker')
obj_1.draw()
obj_2 = Pencil('Jaty')
obj_2.draw()
obj_3 = Handle('Posli')
obj_3.draw()
