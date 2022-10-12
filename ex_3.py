class NotInt(Exception):
    def __init__(self, txt):
        self.txt = txt

li = []
while True:
    a = input('enter data: ')
    if a == 'stop':
        break
    else:
        try:
            if not a.isdigit():
                raise NotInt('not a number')
            # a = int(a)
        except NotInt as err:
            print(err)
        else:
            li.append(int(a))
print(li)
