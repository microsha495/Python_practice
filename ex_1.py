# a = 8
# print(a)
# b = 12
# print(b)
# c = (a + b) // 10
# print(c)
# y = (10 + a + b - c) / 5
# print(y)
# print((10 + a + b - c) // 5)
# print((10 + a + b - c) % 5)
#

cl1 = int(input('введите отметку по предмету 1: '))
cl2 = int(input('введите отметку по предмету 2: '))
cl3 = int(input('введите отметку по предмету 3: '))
cl4 = int(input('введите отметку по предмету 4: '))
print('принято')
print(f'Ваши оценки: предмет 1: {cl1}, предмет 2: {cl2}, предмет 3: {cl3}, предмет 4: {cl4}')
print('Средний балл составляет: ', (cl1 + cl2 + cl3 + cl4) / 4)
