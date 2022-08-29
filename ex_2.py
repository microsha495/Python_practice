time = int(input('Введите время в секундах: '))
hours = time // 3600
mins = (time % 3600) // 60
secs = time - hours * 3600 - mins * 60
print(f'{"{:02d}".format(hours)}:{"{:02d}".format(mins)}:{"{:02d}".format(secs)}')
