# #['Maria Antonovna', 'Anna Igorevna', 'Jeanne Constantinovna']--Teachers
# class School:
#     def __init__(self, classroom_number):
#         self.classroom_number = classroom_number
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Head(Person):
#     def __init__(self, fire_teacher, hire_teacher,teacher_list, give_mark, create_rating, subject):
#         self.fire_teacher = fire_teacher
#         self.hire_teacher = hire_teacher
#         self.teacher_list = teacher_list
#         self.give_mark = give_mark
#         self.create_rating = create_rating
#         self.subject = subject
#
#
#
#
# class Student(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#         self.mark_list = []
#
#
#     def to_get_mark(self, mark):
#         self.mark_list.append(mark)
#
# class Teacher(Person):
#     def __init__(self, name, age, subject, student_list, mark):
#         super().__init__(name, age)
#         self.subject = subject
#         self.student_list = student_list
#         self.mark = []
#
#     def give_mark(self, mark, student_index):
#         for i in self.mark:
#             if i.get(mark):
#                 std = self.student_list[student_index]
#                 std.to_get_mark(i)
#                 print(self.student_list[student_index].mark)
#
#     def create_rating(self):
#         pass
#
#
# class First_year(School):
#     def __init__(self, student_list, teacher, classroom_number):
#         super().__init__(classroom_number)
#         self.student_list = student_list
#         self.teacher = teacher
#
#
#
# class Second_year(School):
#     def __init__(self, student_list, teacher, classroom_number):
#         super().__init__(classroom_number)
#         self.student_list = student_list
#         self.teacher = teacher
#
#
# class Third_year(School):
#     def __init__(self, student_list, teacher, classroom_number):
#         super().__init__(classroom_number)
#         self.student_list = student_list
#         self.teacher = teacher
#
#
#
# a = Student('Pipka', 16, 'Geometry')
# a1 = Student('Piper', 17, 'Geometry')
# a2 = Student('Pipkol', 15, 'Geometry')
#
# b = Teacher('Jeanne Constantinovna', 21, [{'Geometry' : 'Triangle'}], [a,a1,a2], )
#
# b.give_mark(10, 0)



##########################################################################################3



# class A:
#     def hi(self):
#         print('A')
#
# class B(A):
#     def hi(self):
#         print('B')
#
# class C(A):
#     def hi(self):
#         print('C')
#
# class D(B,C):
#     pass
#
# d = D()
#
# d.hi()
#{Поиск в ширину}
# class A1:
#     def hi(self):
#         print('A')
#
# class B1(A1):
#     pass
#
# class C1(A1):
#     #def hi(self):
#         #print('C')
#     pass
# class D1(B1,C1):
#     pass
#
# d = D1()
#
# d.hi()

#######################################################

# Ромбовидное насLедование


# class A_obj:
#     def __init__(self, value):
#         self.__value = value
#
#     def __add__(self, other): #+
#         return self.__value + other.__value
#
#
#     def __eq__(self, other):# ==
#         return self.__value == other.__value
#
#     @staticmethod
#     def show_info():
#         print('pip')
#
#
#
# a1 = A_obj(5)
# a2 = A_obj(0)
# #static method example
# a1.show_info()
# A_obj.show_info()
# print(a1 == a2)
# print(a1+a2)


# class Value:
#     def __init__(self, value):
#         self.__value = value
#
#     def __add__(self, other):  # +
#         return self.__value + other.__value
#
#
#     def __eq__(self, other):# ==
#         return self.__value == other.__value
#
#     def __ge__(self, other): # >=
#         return self.__value >= other.__value
#
#     def __sub__(self, other): # -
#         return self.__value - other.__value
#
#
#     def __mul__(self, other): #*
#         return self.__value * other.__value
#
#
#     def __div__(self, other): #/
#         return self.__value / other.__value
#
#     def __it__(self, other): # <
#         return self.__value < other.__value
#
#     def __le__(self, other): #<=
#         return self.__value <= other.__value
#
#
#     def __ne__(self, other): # !=
#         return self.__value == other.__value
#
#
# class Calc:
#     def __init__(self, a1, a2, operation):
#         self.a1 = a1
#         self.a2 = a2
#         self.operation = operation
#
#         if self.operation == '-':
#             self.b = a1 - a2
#         if self.operation == '+':
#             self.b = a1 + a2
#         if self.operation == '*':
#             self.b = a1 * a2
#         if self.operation == '/':
#             self.b = a1 / a2
#         if self.operation == '==':
#             self.b = a1 == a2
#         if self.operation == '!=':
#             self.b = a1 != a2
#         if self.operation == '<':
#             self.b = a1 < a2
#         if self.operation == '>=':
#             self.b = a1 >= a2
#         if self.operation == '<=':
#             self.b = a1 <= a2
#
#     def result(self):
#         print(self.b)
#
# d1 = Value(3)
# d2 = Value(5)
#
# c = Calc(d1, d2, '+')
# c.result()



import os

#/home/user/Рабочий стол/the_path


class Create:
    # os.listdir("/home/user/Рабочий стол/the_path")
    #
    # path = '/home/user/Рабочий стол/the_path/testpy'
    # os.mkdir(path)
    #
    # os.rename('/home/user/Рабочий стол/the_path', '/home/user/Рабочий стол/by_path/testpy')
    #
    # print(os.listdir("/home/user/Рабочий стол/the_path"))
    # print(os.listdir('/home/user/Рабочий стол/the_path/testpy'))


    # def __init__(self,path):
    #     self.path = path
    #
    # def replace(self):
    #     a = os.listdir("/home/user/Рабочий стол/the_path")
    #     for i in a:
    #         i = i.split('.')
    #         if i == 'txt':
    #             path = '/home/user/Рабочий стол/the_path/txt'
    #             os.mkdir(path)
    #             os.rename('/home/user/Рабочий стол/the_path/file.txt', '/home/user/Рабочий стол/by_path/txt/file.txt')
    #
    a = os.listdir("/home/user/Рабочий стол/the_path")
    for i in a:
        i = i.split('.')
        if i == 'txt':
            path = '/home/user/Рабочий стол/the_path/txt'
            os.mkdirs(path)
            os.rename('/home/user/Рабочий стол/the_path/file.txt', '/home/user/Рабочий стол/by_path/txt/file.txt')
        else:
            print('none')











