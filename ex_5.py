revenue = float(input('Выручка: '))
costs = float(input('Издержки: '))
if revenue > costs:
    profit = revenue - costs
    print('Прибыль составила: ', profit)
    rent = profit / revenue * 100
    print('Рентабельность выручки: ', "%.2f" % (rent), '%')
    num_emp = int(input('Укажите количество сотрудников: '))
    print('Прибыль на одного сотрудника составила: ', "%.2f" % (profit / num_emp))
elif revenue < costs:
    print('Убыток составил: ', costs - revenue)
else:
    print('Прибыль равна убытку')