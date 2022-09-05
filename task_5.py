li = []
count = int(input('введите количество операций: '))
for n in range(0, count):
    num = int(input('введите число: '))
    idx = 0
    if len(li) == 0:
        li.append(num)
    else:
        for i in range(0, len(li)):
            if li[i] < num:
                li.insert(i, num)
                idx = i
                break
            elif li[i] == num:
                idx = i + li.count(li[i])
                li.insert(idx, num)
                break
            elif li[len(li) - 1] > num:
                li.append(num)
                idx = len(li) - 1
                break
            else:
               continue
    print(f'Текущий список: {li}. Индекс добавленного числа: {idx}.')
