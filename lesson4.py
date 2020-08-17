import math
#num = int(input("Factorial:"))
#factorial = 1
#for i in range(1, num+1):
#    factorial = factorial * i
#print(factorial)


#num = int(input(("factorial: ")))
#factorial = 1
#while num!=0:
#    factorial = factorial * num
#    num = num -1
#print(factorial)


##a_list = [1, 2, 3, 4]
##sum = 0
##for i in a_list:
##    sum = sum + i
##print(sum)


##a_list = [1, 2, 3, 4]
##sum = 0
##while a_list:
##    sum = sum + a_list.pop()
##print(sum)


#a_list = [1,2,3]
#b_list = [11,22,33]
#i = 0
#j = 0
#c_list = []
#for el in range(len(a_list)+len(b_list)):
#    if el%2 == 0:
#        c_list.insert(j+2,a_list[i])
#       i = j+1
#    else:
#        c_list.insert(i*3, b_list[j])
#        j += 1
#    print(c_list)
#print(c_list)

#a_l = int(input("Введите сторону А:"))
#b_l = int(input("Введите сторону В:"))
#c_l = int(input("Введите сторону С:"))
#if (a_l+b_l) > c_l:
#    print("Существует")
#elif (c_l+a_l) > b_l:
#    print("существует")
#else:
#    print("No")


#m = int(input("Введите кол-во строк: "))
#a_list = []
#for i in range(m):
#    a_str = input("Введите строку: ")
#    a_list.append(a_str.replace('?','*'))
#print(a_list)


#a = "2009-06-15"
#b = "{}/{}/{}"
#a_list = a.split('-')
#a_list.reverse()
#b.format(a_list[0], a_list[1], a_list[2])
#print(b.format(a_list[0], a_list[1], a_list[2]))


#a = int(input("Введите вес: "))
#a_copy = a
#b = a / 1000
#c = a_copy / 10000
#print("Ваш вес в тоннах - ",c)
#print("Ваш вес в килограммах - ",b)


# a = int(input("Введите высоту коробки: "))
# b = int(input("Введите ширину коробки: "))
# c = int(input("Введите длинну коробки: "))
# a_d = 90
# b_d = 50
# if a < a_d and b < b_d:
#     print("Коробка пройдёт.")
# elif c < a_d and b < b_d:
#     print("Коробка пройдёт.")
# else:
#     print("Нет")


a = int(input("Введите ширину бруса: "))
d = float(input("Введите диаметр бревна: "))
c = math.sqrt(a*a*2)
if c<=d:
    print("Можем")
else:
    print("Нет")




