class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        print(self.name + ' ' + self.surname)
    def get_total_income(self):
        print('total_income = ', self._income['wage'] + self._income['bonus'])


worker_1 = Position('Alex', 'Bell', 'worker', 3500, 500)
print(f'''
name: {worker_1.name}
surname: {worker_1.surname}
position: {worker_1.position}
income: {worker_1._income}''')
worker_1.get_full_name()
worker_1.get_total_income()
