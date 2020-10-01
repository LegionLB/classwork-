import os
#
# #принимает путь к папке, показать список всех компонентов в этой папке
#
# class Show:
#
#     def __init__(self, name_path):
#         self.name_path = name_path
#         self.__counter = 0
#         self.a_dir = os.listdir(self.name_path)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < len(self.a_dir):
#             cur_file = self.a_dir[self.__counter]
#             self.__counter += 1
#             return cur_file
#         else:
#             raise StopIteration
#
# dir = Show("/home/user/Рабочий стол/the_path")
# for i in dir:
#     print(i)
# принимает путь к файлу, найти самый часто используемый символ и заменить на *, создать новый файл с измен
#========================================
class Changer:

    def __init__(self, path):
        self.__path = path

    def file(self):
        f = open(self.__path, 'r')
        #из строки в лист из листа в сэт(каунтим кол-во)
        fd = f.read()



a = Changer(//home//user//Рабочий стол//the_path//txt//123.txt)
a.file()

#
#========================================



# def fibo_generator(num):
#     n1 = 1
#     n2 = 1
#     counted = 0
#     while counted < num:
#         res = n1 + n2
#         n1 = n2
#         n2 = res
#         yield res
#         counted += 1
#
# a = fibo_generator(5)
# for i in a:
#     print(i)