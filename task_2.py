#способ_1
li = list(input('введите список: '))
print('old list: ', li)
for i in range(1, len(li), 2):
    li[i], li[i - 1] = li[i - 1], li[i]
print('new list: ', li)


#способ_2
# li = list(input('введите список: '))
# print('old list: ', li)
# for i in range(1, len(li), 2):
#     temp = li[i]
#     li[i] = li[i - 1]
#     li[i - 1] = temp
# print('new list: ', li)