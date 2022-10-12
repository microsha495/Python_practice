class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input('enter number: '))
b = int(input('enter number: '))

try:
    if b == 0:
        raise ZeroDiv('Division by zero is prohibited')
    res = a / b
except (ZeroDiv) as err:
    print(err)
else:
    print(f'{a} / {b} = {res}')


