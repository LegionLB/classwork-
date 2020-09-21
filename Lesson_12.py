
#фунция принимае дату проверить есть ли она такая дэйтайм try/exept
#======================================================================

# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def display_info(self):
#         print("Name: {}\n Surname: {}\n Age: {} \n".format(self.name, self.surname, self.age))
#
#
# class Employee(Person):
#     def __init__(self, name, surname, age, company):
#         Person.__init__(self, name, surname, age)
#         self.company = company
#
#     def display_info(self):
#         Person.display_info(self)
#         print("Company: {}".format(self.company))
#
#
#
# p = Person("Nick", "Test", 22)
# e = Employee("Nick", "Test2", 23, "Tesla")
#
#
# p.display_info()
# e.display_info()

class EmailError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = self.validate(email)

    def validate(self, email):
        if "@" and "." not in email:
            raise EmailError("Invalid email")
        return email


u1 = User("name", "User@email.com")
u2 = User("invalid", "invalidemail")

#Homework
#-Есть файл, считать инфу, определить кол-во символов, слов, предложений
#-Есть класс "Юзер", метод Дампинфо, создает файл и записывает всю инфу про пользователя построчно,
# есть функция - возвращает нового пользователя
#-Сделать правильную валидацию имейла
#-
#-
