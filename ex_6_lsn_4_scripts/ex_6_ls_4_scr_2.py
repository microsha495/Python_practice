from itertools import cycle

def my_cycle(li, max):
    i = 0
    for el in cycle(li):
        print(el)
        i += 1
        if i == max:
            break
