from random import randint
start_list = [randint(1, 100) for i in range(0, 10)]
new_list = [el for el in start_list if start_list.count(el) == 1]
print(start_list)
print(new_list)