#массив  поменять местами чётные и нет

# a = int(input('Введите массив: '))
# list_res = list()
# for i in range(a):
#     list_res.append(input('Element {}: ' .format(i))) #skobki shablon
#
# for i in range(a):
#     if  i % 2 == 0 and i+1<a:
#         list_res[i]. list_res[i+1] = list_res[i+1]. list[i]
#
# print(list_res) #################dodelat


# int_a = int(input('Input start: '))
# int_b = int(input('Input end: '))
#
# def func(a,b):
#     list_simple = list()
#     for el in range(a, b+1):
#         counter = 0
#         tmp_simple = el
#         while tmp_simple>0:
#             if el % tmp_simple == 0:
#                 counter += 1
#              tmp_simple -= 1
#
#         if counter == 2:
#             list_simple.append(el)
#     return list_simple
#
# print(func(int_a, int_b))


# list_a = [el for el in range(1,6)]# sposob zapisi

# print(list_a)


list_a = list()#norm sposob
for el in range(10):
    list_a.append(el)

list_a = [el for el in range(10)] # uproschenn