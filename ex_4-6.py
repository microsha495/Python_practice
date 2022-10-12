class EquipmentStock:
    def __init__(self):
        self.inv = {}

    def accept_to_stock(self, OfficeEquipment):
        self.inv.setdefault(OfficeEquipment.get_eqp_name(), []).append(OfficeEquipment)

    def move_to_dept(self, acc_num):
        for key, value in self.inv.items():
            for el in value:
                if acc_num == el.acc_num:
                    print(f'delete......... {el}')
                    value.remove(el)

    def Print(self):
        print(sum(len(val) for val in self.inv.values()))
        for key, value in self.inv.items():
            print(f'{key} ({len(value)}):')
            for el in value:
                print(f'\t{el}')


class OfficeEquipment:
    def __init__(self, name, serial_num, account_num):
        self.name = name
        self.ser_num = serial_num
        self.acc_num = int(account_num)
        self.eqp_name = self.__class__.__name__

    def get_eqp_name(self):
        return f'{self.eqp_name}'


class MFU(OfficeEquipment):
    def __init__(self, name, serial_num, account_num, scan_option, xerox_option):
        super().__init__(name, serial_num, account_num)
        self.sc_opt = scan_option
        self.xr_opt = xerox_option

    def __str__(self):
        return f'name: {self.name}, ser.num.: {self.ser_num}, acc.num.: {self.acc_num}, scan.option: {self.sc_opt}, xerox option: {self.xr_opt}'


class PC(OfficeEquipment):
    def __init__(self, name, serial_num, account_num, monitor, keyboard, mouse):
        super().__init__(name, serial_num, account_num)
        self.mon = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __repr__(self):
        return f'name: {self.name}, ser.num.: {self.ser_num}, acc.num.: {self.acc_num}, monitor: {self.mon}, keyboard: {self.keyboard}, mouse: {self.mouse}'


class PhoneFax(OfficeEquipment):
    def __init__(self, name, serial_num, account_num, radio, fax_option):
        super().__init__(name, serial_num, account_num)
        self.radio = radio
        self.fax_opt = fax_option

    def __repr__(self):
        return f'name: {self.name}, ser.num.: {self.ser_num}, acc.num.: {self.acc_num}, radiophone: {self.radio}, fax option: {self.fax_opt}'


stock1 = EquipmentStock()
mfu1 = MFU('Canon', '12345MF', 4567896, 'Y', 'Y')
stock1.accept_to_stock(mfu1)
mfu2 = MFU('Canon', '12gj5MF', 434680, 'N', 'Y')
stock1.accept_to_stock(mfu2)
pc1 = PC('Dell', '109ft', 456235, 'Y', 'Y', 'Y')
mfu3 = MFU('Canon', '12345MF', 456789, 'Y', 'Y')
stock1.accept_to_stock(mfu3)
stock1.accept_to_stock(pc1)
phone1 = PhoneFax('Tele2', '12349j', 8967453, 'Y', 'N')
stock1.accept_to_stock(phone1)
pc2 = PC('Asus', '12ldsc', 434786, 'Y', 'Y', 'N')
stock1.accept_to_stock(pc2)
stock1.Print()


stock1.move_to_dept(456789)
stock1.Print()
