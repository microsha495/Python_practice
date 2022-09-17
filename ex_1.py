from sys import argv
work_hours, zpl_hour, prem = map(int, argv[1:])
print('Зарплата сотрудника: ', work_hours * zpl_hour + prem)