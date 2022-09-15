old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [old[i] for i in range(len(old)) if old[i] > old[i - 1]]
print(old)
print(new)