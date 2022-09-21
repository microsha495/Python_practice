with open('text_for_ex_2.txt', 'w+', encoding='utf-8') as txt_file:
    str_list = ['привет\n', 'как дела?\n', 'до свидания, всего хорошего']
    txt_file.writelines(str_list)
    txt_file.seek(0)
    str_read = txt_file.read().split('\n')
    print(str_read)
    print('количество строк: ', len(str_read))
    i = 0
    for el in str_read:
        i += 1
        print(f'количество слов в строке {i}: ', len(el.split()))
