
#задача 1***************************************************************************

def dividing(a, b):
    try:
        print('result=', float(a) / float(b))
    except ZeroDivisionError:
        print('cannot divide by zero')
    except ValueError:
        print('enter only numbers')

a = input('enter num_1: ')
b = input('enter num_2: ')

dividing(a, b)


#задача 2***************************************************************************

def info(name, surname, year_of_birth, city, email, teleph):
    print(f'''
    Name: {name}
    Surname: {surname}
    City: {city}
    Year of birth: {year_of_birth}
    E-mail: {email}
    Phone number: {teleph}
''')

info(name=input('enter name: ', ), surname=input('enter surname: ', ), year_of_birth=input('enter year of birth: ', ), city=input('enter city: ', ), email=input('enter email: ', ), teleph=input('enter phone number: '))


#задача 3***************************************************************************

def my_func(a, b, c):
    nums = [a, b, c]
    nums.sort(reverse=True)
    try:
        print(float(nums[0]) + float(nums[1]))
    except ValueError:
        print('enter only numbers')

my_func(input('enter a: '), input('enter b: '), input('enter c: '))


#задача 4, способ 1***************************************************************************

def my_func(x, y):
    print('res = ', x ** y)

my_func(float(input('enter x: ')), int(input('enter y: ')))


#задача 4, способ 2***************************************************************************

def my_func(x, y):
    res = 1
    for i in range(y, 0):
        res *= (1 / x)
    print('res = ', res)

my_func(float(input('enter x: ')), int(input('enter y: ')))


#задача 5***************************************************************************

result_list = []
summa = 0
while True:
    num_str = input('enter numbers separated by a space (enter s to stop): ').split()
    isSpecSymb = False
    for num in num_str:
        if num == 's':
            isSpecSymb = True
            break
        else:
            summa += float(num)
    print('result=', summa)
    if isSpecSymb == True:
        break


#задача 6+7***************************************************************************

def int_func():
    words = input('enter words: ')
    isSpecSymb = False
    for symbol in words:
        if symbol == ' ' or ord(symbol) in range(97, 123):
            continue
        else:
            isSpecSymb = True
            break
    if isSpecSymb == True:
        print('Please, use only low latin letter')
    else:
        print(words.title())

int_func()