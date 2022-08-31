n = int(input('введите число: '))
max = -1
while n > 0:
    temp = n % 10
    n //= 10
    if temp > max:
        max = temp
print('максимальная цифра = ', max)