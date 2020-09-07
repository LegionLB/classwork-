# class Car:
#     def __init__(self, power, max_speed):
#         self.power = power
#         self.max_speed = max_speed
#
#     @property
#     def max_speed(self):
#         return self.max_speed
#
#     @property
#     def power(self):
#         return self.power
#
# class Bus(Car):
#     def __init__(self, power, max_speed, count, color):
#         print('Bus init')
#         Car.__init__(self, power, max_speed)
#         self.__count = count
#         self.color = color
#         #self.not_free_seats = not_free_seats
#
#     def not_free_seatss(self):
#         enter_man = int(input('Input count of passengers: '))
#         for i in range(1, enter_man+1):
#             if i <= self.__count:
#                 a = self.__count - enter_man
#                 print('This count of people can in.')
#             else:
#                 print('This count of people can'"t"' in')
#
#     def show_info(self):
#         print('Max speed is {}, hp - {}, seats {}'.format(self.power, self.max_speed, self.__count))
#
# b = Bus(500, '100mph', 5, 'White')
# b.not_free_seatss()
# b.show_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Teacher(Person):
    def __init__(self, name, age, knowledge, list_students):
        super().__init__(name, age)
        self.knowledge = knowledge
        self.list_students = list_students

    def to_teach(self, knowledge, student_index):
        for i in self.knowledge:
            if i.get(knowledge):
                self.list_students[student_index].to_get_knowledge(i)
                print(self.list_students[student_index].knowledge)




class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.knowledge = []

    def to_get_knowledge(self, knowledge):
        self.knowledge.append(knowledge)

c1 = Student('Pepper', 16)
c2 = Student('Pepp', 15)
c3 = Student('Per', 17)
b = Teacher('Anna', 29, [{'Geometry' : 'Triangle'}], [c1,c2,c3])

b.to_teach('Geometry', 0)

