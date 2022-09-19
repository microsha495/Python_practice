with open('text_for_ex4.txt', 'r') as txt_file:
    eng_txt = txt_file.readlines()
    dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open('new_text_for_ex4.txt', 'a', encoding='utf-8') as txt_new:
        for el in eng_txt:
            inner_list = el.strip('\n').split(' - ')
            txt_new.write(f'{dictionary.get(inner_list[0])} - {inner_list[1]}\n')
