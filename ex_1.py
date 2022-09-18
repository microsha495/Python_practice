with open("text_for_ex1.txt", 'a', encoding='utf-8') as txt_file:
    while True:
        data = input('введите данные: ')
        if not data:
            break
        txt_file.write(data + '\n')
