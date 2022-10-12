class Date:
    def __init__(self, dd, mm, yyyy):
        self.d = dd
        self.m = mm
        self.y = yyyy
    @classmethod
    def set_date(cls, date_str):
        date_li = date_str.split('-')
        d, m, y = date_li
        return cls(int(d), int(m), int(y))
    @staticmethod
    def check_date(obj):
        if obj.m in [1, 3, 5, 7, 8, 10, 12]:
            if obj.d not in range(1, 32):
                print('Incorrect data. Please check')
                return
        elif obj.m in [4, 6, 9, 11]:
            if obj.d not in range(1, 31):
                print('Incorrect data. Please check')
                return
        elif obj.m == 2:
            if obj.d not in range(1, 30):
                print('Incorrect data. Please check')
                return
        if obj.y < 1000 or obj.y > 2022:
            print('Incorrect data. Please check')
            return

    def __str__(self):
        return f'dd-mm-yyyy: {"%02d" % self.d}-{"%02d" % self.m}-{self.y}'

date = '01-02-1994'
d = Date.set_date(date)
print(d.d, d.m, d.y)
date2 = '28-02-999'
d2 = Date.set_date(date2)
d2.check_date(d2)
print(d2)