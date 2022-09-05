li = input('введите строку: ').split()
for n, el in enumerate(li, 1):
    print(n, '. ', el[:10])