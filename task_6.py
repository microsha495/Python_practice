li = []
i = 1
while True:
    di = {}
    di['название'] = input('введите название товара: ')
    di['цена'] = input('введите цену товара: ')
    di['количество'] = input('введите количество товара: ')
    di['ед'] = input('введите единицы измерения количества товара (шт., уп. и др.): ')
    li.append((i, di))
    a = input('продолжить ввод? да/нет : ').lower()
    if a == 'нет':
        break
    i += 1
print('Список товаров')
for el in li:
    print(el)
di_analyse = {}
for el in li:
    for key_x, value_x in el[1].items():
        if di_analyse.get(key_x) == None:
            di_analyse[key_x] = [value_x]
        else:
            if key_x == 'ед':
                if value_x not in di_analyse[key_x]:
                    di_analyse[key_x].append(value_x)
                else:
                    continue
            else:
                di_analyse[key_x].append(value_x)
print('Аналитика по товарам')
for key, value in di_analyse.items():
    print(f'{key}:{value}')