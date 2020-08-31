# class Car:
#
#     def __init__(self, max_speed, seats, mark, color):
#         self.max_speed = max_speed
#         self.seats = seats
#         self.mark = mark
#         self.color = color
#         self.free_seats = self.seats - 1
#
#     def add_man(self):
#         if self.free_seats > 0:
#             self.free_seats -= 1
#             print('Added one passenger')
#         else:
#             print('Car is full')
#
#
#
#
# car = Car(150, 5, 'Audi', 'Yellow')
# car.add_man()
# car.free_seats = 10
# car.add_man()
# car.add_man()
# print(car.free_seats)
# car.add_man()
# car.add_man()


# person_list = []
# person_count = int(input('Input person count: '))
#
#
# class Person:
#
#     def __init__(self, name, age, phone_number):
#         self.name = name
#         self.age = age
#         self.phone_number = phone_number
#
#     def __str__(self):
#         return self.name + '/' + self.age + '/' + self.phone_number
#
#
# def person():
#     print('Please input the information(name, age, phone number): ')
#     name = input('Input name: ')
#     age = input('Input age: ')
#     phone_number = input('Input phone number: ')
#     p = Person(name, age, phone_number)
#     return str(p)
#
#
# for i in range(person_count):
#     person_list.append(person())
#
#
# print(person_list)

# class Car:
#
#     raw = 0
#
#     def __init__(self, max_speed, seats, mark, color):
#         self.max_speed = max_speed
#         self.seats = seats
#         self.mark = mark
#         self.color = color
#         self.__free_seats = self.seats - 1
#
#     def add_man(self):
#         if self.free_seats > 0:
#             self.free_seats -= 1
#             print('Added one passenger')
#         else:
#             print('Car is full')
#         Car.raw = 1
#
#
#
# car = Car(150, 5, 'Audi', 'Yellow')

# print(car.raw)
# car.add_man()
# print(car.raw)
#
# car2 = Car(50,3,'BMW','Black')
# print(car2.raw)
# car2.raw = 10
# print(car2.raw)
# print(car2.raw)

#print(dir(car))
#print(help(car))


#print(car._Car__free_seats)
person_list = []
person_count = int(input('Input person count: '))


class Person:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + '/' + self.age + '/' + self.phone_number


def person():
    print('Please input the information(name, age, phone number): ')
    name = input('Input name: ')
    age = int(input('Input the year of birth: '))
    phone_number = input('Input phone number: ')
    p = Person(name, age, phone_number)
    return p


for i in range(person_count):
    person_list.append(person())



print(person_list)

for j in person_list:
    if j.age > 1990:
        person_list.remove(j)


print(person_list[0])



