class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width
    def mass(self):
        print(f'масса асфальта = {(self._lenght * self._width * 25 * 5) / 1000}т')


road_1 = Road(20, 5000)
road_1.mass()
