def fact(n):
    if n == 0:
        print('0! = 1')
    elif n < 0:
        print('n must be >= 0')
    else:
        f = 1
        for el in range(1, n + 1):
            f *= el
            yield f

i = 0
for el in fact(10):
    i += 1
    print(f'{i}!={el}')


