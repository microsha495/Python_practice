with open('text_for_ex6.txt', 'r', encoding='utf-8') as txt_file:
    li_1 = txt_file.read().split('\n')
    subj_dict = {}
    for el in li_1:
        subj_li = el.split()
        subj_hours = 0
        for n in subj_li[1:]:
            if n == '—':
                pass
            else:
                subj_hours += int(n.strip('(лпраб)'))
        subj_dict.update({subj_li[0].strip(':'): subj_hours})

    print(subj_dict)
