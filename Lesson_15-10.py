#почитать про секции JOIN
# файлик  (имя , число, месяц, год) вывести в каком веке кто родился
# дикт ключ - век, значение - список имен

f = open('/home/user/Рабочий стол/the_path/zadanie', 'r')
lines = f.readlines()
for i in lines:
    lines_str = i.split(' ')
    lines_str.pop(0)
    lines_str.pop(0)
    for j in lines_str:
        num_str = j.split('.')
        num_str.pop(0)
        num_str.pop(0)
        for n in num_str:
            dates = n.split("\n")
            dates.pop(-1)

            print(dates)
            if int(n) > 2000:
                cen21 = list()
                cen21.append(n)
                print("21 century")
            elif int(n) <= 2000:
                cen20 = list()
                cen20.append(n)
                print('20 century')





