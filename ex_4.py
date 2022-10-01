class Car:
    def __init__(self, speed, color, name, bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool
    def go(self):
        print(f'{self.name} goes')
    def stop(self):
        print(f'{self.name} stops')
    def turn(self, a):
        if a == 'r':
            print(f'{self.name} turned right')
        elif a == 'l':
            print(f'{self.name} turned left')
    def show_speed(self):
        print(f'{self.name} speed is: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, bool):
        super().__init__(speed, color, name, bool)
    def show_speed(self):
        if self.speed > 60:
            print('speed is exceeded')
        else:
            print(f'{self.name} speed is: {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, bool):
        super().__init__(speed, color, name, bool)

class WorkCar(Car):
    def __init__(self, speed, color, name, bool):
        super().__init__(speed, color, name, bool)
    def show_speed(self):
        if self.speed > 40:
            print('speed is exceeded')
        else:
            print(f'{self.name} speed is: {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, bool):
        super().__init__(speed, color, name, bool)

car_1 = TownCar(55, 'red', 'Mazda', False)
print(f'Speed of {car_1.color} {car_1.name} is {car_1.speed}. Police car : {car_1.is_police}')
car_1.go()
car_1.show_speed()
car_1.turn('r')
car_1.stop()
car_2 = TownCar(70, 'black', 'BMW', False)
car_2.go()
car_2.show_speed()
car_2.turn('l')
car_2.stop()
car_3 = SportCar(100, 'yellow', 'Lamborgini', False)
car_3.go()
car_3.show_speed()
car_3.turn('r')
car_3.stop()
car_4 = WorkCar(60, 'blue', 'WV', False)
car_4.go()
car_4.show_speed()
car_4.turn('l')
car_4.stop()
car_5 = PoliceCar(80, 'white', 'Geely', True)
print(f'Speed of {car_5.color} {car_5.name} is {car_5.speed}. Police car : {car_5.is_police}')
car_5.go()
car_5.show_speed()
car_5.turn('l')
car_5.stop()
