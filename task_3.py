# #var_1
month = int(input('введите номер месяца: '))
di = {'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11], 'зима': [12, 1, 2]}
for el in di:
    if month in di[el]:
        print(el)
        break

#var_2
months = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
mon = int(input('введите номер месяца: '))
for n, el in enumerate(months, 1):
    if mon in el:
        print('весна' if n == 1 else 'лето' if n == 2 else 'осень' if n == 3 else 'зима')
        break
