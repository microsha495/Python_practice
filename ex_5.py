with open('text_for_ex5.txt', 'w+') as txt_file:
    txt_file.write(input('enter numbers by space: '))
    txt_file.seek(0)
    li = txt_file.read().split()
    print(li)
    summ = 0
    for num in li:
        try:
            summ += float(num)
        except ValueError:
            print(f'<{num}> was not a number')
            pass
    print(f'summ = {summ}')