from functools import reduce
li = [i for i in range(100, 1001, 2)]
def my_func(el, next_el):
    return el * next_el
print(f'result = {reduce(my_func, li)}')