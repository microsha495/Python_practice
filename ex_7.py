import json
with open('text_for_ex7.txt', 'w+') as txt_file:
    li_to_write = ['firm_1 OOO 10000 5000\n', 'firm_2 OAO 20000 15000\n', 'firm_3 OOO 5000 10000\n', 'firm_4 OAO 10000 10000']
    txt_file.writelines(li_to_write)
    txt_file.seek(0)
    common_profit = 0
    count_prof_firms = 0
    result_li = []
    firms_di = {}
    for line in txt_file.readlines():
        comp_info = line.split()
        if int(comp_info[2]) > int(comp_info[3]):
            print(f'profit of {comp_info[0]} = {int(comp_info[2]) - int(comp_info[3])}')
            common_profit += int(comp_info[2]) - int(comp_info[3])
            count_prof_firms += 1
            firms_di.update({comp_info[0]: (int(comp_info[2]) - int(comp_info[3]))})
        elif int(comp_info[2]) == int(comp_info[3]):
            print(f'profit of {comp_info[0]} is equal to the costs')
            firms_di.update({comp_info[0]: (int(comp_info[2]) - int(comp_info[3]))})
        else:
            print(f'loss of {comp_info[0]} = {int(comp_info[2]) - int(comp_info[3])}')
            firms_di.update({comp_info[0]: (int(comp_info[2]) - int(comp_info[3]))})
    average_profit = common_profit / count_prof_firms
    result_li.append(firms_di)
    result_li.append({'average_profit': average_profit})
    print(result_li)
    with open('ex_7_json.json', 'w') as f:
        json.dump(result_li, f)
