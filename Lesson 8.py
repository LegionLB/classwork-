#1================================================
#Возвести числа в степень до заданного предела
# num = int(input('Input a number: '))
# s1 = int(input('INput start"*": '))
# s2 = int(input('INput end "*": '))
#
#
# def up(a,b,c):
#     a_list = []
#     for i in range(a, b+1):
#         a_list.append(c ** i)
#     return a_list
# print(up(num, s1, s2))

#2=================================================
# sum 1234---->10

# num = input('Input num: ')
#
# def plus(a):
#     sum = 0
#     a_list = list(a)
#     for el in a_list:
#         sum += int(el)
#     return sum
#
# print(plus(num))

#3=================================================
#reverse number

# num = input('INput num: ')
#
# def reverse(a):
#     b = ''
#     a_list = list(a)
#     a_list.reverse()
#     b = ''.join(a_list)
#     print(b)
#     return b
# reverse(num)

#4==================================================
#fibonachi
# [1,1] ---->[1,1,2] ----> [1,1,2,3]


# def fib(a):
#     a_list = [1,1]
#     while a:
#         b = a_list[-1] + a_list[-2]
#         a_list.append(b)
#         a-=1
#     return a_list
# print(fib(5))# вечный фибо


#5==================================================
# sum 2

# num = input('Input num: ')
#
# def plus(a):
#     sum = 0
#     sum2 = 1
#     a_list = list(a)
#     for el in a_list:
#         sum += int(el)
#         sum2 *= int(el)
#     return sum, sum2
#
# print(plus(num))

#6==========================================
#buble

a_list = [1,2,3,4,5,6,7,8,9,10]

def sort(a):
    l = len(a)
    for i in range(l):
        for j in range(0, l-i-1):
            if a[j] > a[j + 1]:
                b = a[j]
                a[j] = a[j + 1]
                a[j + 1] = b
            return l

print(sort(a_list))












