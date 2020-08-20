# def func_dict(dict_a, value):
#     dict_a.update({"key" : value})
#     print("IN function dict is: ")
#     print(dict_a)
#
# c = input("Input value: ")
# start_dict = {"key1" : 1, "key2" : 2}
# func_dict(start_dict,c)
# print(start_dict)

# default_list = [1,2,3,4,5,6,7,8,9]
# def list_sum(a_list, sum=0):
#     if a_list:
#         sum += a_list.pop()
#         print(sum)
#         return list_sum(a_list,sum)
#     else:
#         return sum
# list_sum(a_list=default_list)

#default_list = [1,2,3,4,5,6,7,8,9]
#def list_sum(a_list, sum=0):
#     for i in a_list:
#         sum = sum + i
#         print(sum)
#     return sum
# list_sum(a_list=default_list)

# default_list = [1,2,3,4,5,6,7,8,9]
# def list_sum(a_list, sum=0):
#     while a_list:
#         sum += a_list.pop()
#         print(sum)
#     return sum
# list_sum(a_list=default_list)





# a_list = [1,2,3]
# b_list = [11,22,33]
# c_list = []
# def list_add(a_list, b_list):
#     for i in range(len(a_list)):
#         c_list.append(a_list[i])
#         c_list.append(b_list[i])
#     return c_list
# print(list_add(a_list, b_list))
#        while a_list and b_list:
#            c_list.append(a_list.pop(0))
#            c_list.append(b_list.pop(0))
#         return c_list
# print(list_add(a_list, b_list))


# def decorator_plus(func_to_decorate):
#     def wrapper():
#         print("+++++++++++++++++")
#         func_to_decorate()
#         print("+++++++++++++++++")
#     return wrapper
#
#
# def decorator_line(func_to_decorate):
#     def wrapper():
#         print("-----------------")
#         func_to_decorate()
#         print("-----------------")
#     return wrapper
# @decorator_line
# @decorator_plus
# def print_name():
#     print("hello , user")
# print_name()


a = "2009-06-15"
b = "{}/{}/{}"
def super_str(a , b):
    a_list = a.split('-')
    a_list.reverse()
    b = b.format(a_list[0], a_list[1], a_list[2])
    return b
print(super_str(a,b))
