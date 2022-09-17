from itertools import count

def my_count(start, end):
    for el in count(start):
        if el > end:
            break
        print(el)
