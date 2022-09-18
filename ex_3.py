with open('text_for_ex3.txt', 'w+', encoding='utf-8') as txt_file:
    str_list = ['Иванов 23456.78\n', 'Петров 15768.45\n', 'Сидоров 78456.34\n', 'Кочанова 23453.87\n', 'Веселова 345987.12\n', 'Юзуфов 7612.56\n', 'Таранов 34987.13\n', 'Васькин 67345.0\n', 'Здраднов 12326.55\n', 'Ошмян 44566.86']
    txt_file.writelines(str_list)
    txt_file.seek(0)
    print(txt_file.read())
    txt_file.seek(0)
    str_read = txt_file.read().split('\n')
    low_slr = []
    summ = 0
    for el in str_read:
        n = el.split()
        slr = float(n[1])
        summ += slr
        if slr < 20000:
            low_slr.append(n[0])
    print(f'Сотрудники с зарплатой ниже 20000: {low_slr}')
    print(f'Средний доход сотрудников: {round(summ / len(str_read), 2)}')
