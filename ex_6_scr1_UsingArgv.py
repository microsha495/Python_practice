from sys import argv
from itertools import count

start, end = map(int, argv[1:])
def my_count(start, end):
    for el in count(start):
        if el > end:
            break
        print(el)

my_count(start, end)