# class Student:
#     # # pass
#     # age = 24
#     # name = 'Aboba'
#
#
# some_stud = Student()
# other_stud = Student()
#
# other_stud.name = 'Федор'
# other_stud.age = 21
#
#
# print(some_stud.name)
# print(some_stud.age)
#
# print("--------")
#
# print(other_stud.name)
# print(other_stud.age)
#
# gg = Student()
#
# print(gg.age)


a = 1

# class Stud:
#     spec = 'Comp Science'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_in_f(self):
#         return f'Student {self.name}, age - {self.age}, spec - {self.spec}'
#
#     def show_msg(self, msg_text):
#         return f"{self.name} saying {msg_text}"
#
#
# artur = Stud('Alexey', 17)
#
# ss = Stud('Ice', 25)
#
# print(f"{artur.spec} --- {artur.name} --- {artur.age}")
# print(f"{ss.spec} --- {ss.name} ------ {ss.age}")
#
#
# print(artur.show_in_f())
# print(artur.show_msg(input("-")))

b = 2

import random
from datetime import date


class Person:
    hobby = "cooking"

    def __init__(self, name, last_name, age):
        self.name = name
        self._age = age
        self.lastName = last_name
        # self.__id = [random.randint(1, 100) for _ in range(6)]
        self.__id = random.randint(10 ** 5, 10 ** 6)

    def change_age(self, new_age):
        self._age = new_age

    def __get_id(self):
        return str(self.__id)

    def _get_full_name(self):
        return f"{self.name} {self.lastName}"

    def getInfo(self):
        return f"Name - {self.name}\nLast Name - {self.lastName}\nAge - {self._age}\nID -> {self.__get_id()}"

    def getHi(self, text_msg):
        return f"{self.getInfo()}\n-----\nHi, I`m {self.name}, {text_msg}\n-----\nID ->{self.__get_id()}<-"

    @classmethod
    def setDefaultHobby(cls):
        cls.hobby = "Drawing"

    @classmethod
    def basedOnBYear(cls, name, last_name, bYear):
        personAge = date.today().year - bYear

        return cls(name, last_name, personAge)

    @classmethod
    def basedOnStr(cls, string):
        name, last_name, age = string.split()
        age = int(age)
        return cls(name, last_name, age)

    @staticmethod
    def sayGreetings():
        print("Nice to meet you!")


class Student(Person):
    def __init__(self, name, last_name, age, mark):
        super().__init__(name, last_name, age)
        self.mark = mark

    def getInfo(self):
        return f"{super().getInfo()}\nMark - {self.mark}"

    def is_successful(self, time_mark):
        # good = True if mark >= 8 else False
        good = time_mark >= 8
        return f"{self.name} с входным баллом {self.mark} successful? >>>{good}<<<"


class Employee(Person):
    def __init__(self, name, last_name, age, job_title, salary, seniority):
        super().__init__(name, last_name, age)
        self.job_title = job_title
        self.salary = salary
        self.seniority = seniority

    def getInfo(self):
        return f"{super().getInfo()}\n---------\nJob Title ->{self.job_title}\nSalary ->{self.salary}\nSeniority" \
               f" ->{self.seniority}\n"

    def is_retiree(self):
        return self._age > 62

    def sick_salary_calc(self, percent):
        sick_salary = (self.salary * percent) / 100
        if sick_salary.is_integer():
            return int(sick_salary)
        return sick_salary

    def get_sick_leave_perc(self):
        if self.seniority >= 5:
            percent = 100
        elif 3 <= self.seniority < 5:
            percent = 75
        else:
            percent = 50
        if self.is_retiree():
            return f"{self.name} {self.lastName} находится на пенсии, какие больничные выплаты"
        return f"У {self.name} {self.lastName} процент от ЗП на больничном будет равен {percent}%, значит выплата " \
               f"будет равна {self.sick_salary_calc(percent)}"


class Developer(Person):
    __rung = "Trainee - free job power"

    _current_salary = 0

    def __init__(self, name, last_name, age, percent, job_title):
        super().__init__(name, last_name, age)
        self.job_title = job_title
        self.base_salary = Developer._current_salary
        self.__rung = Developer.__rung
        self.percent = percent

    positions = ["Junior", "Middle", "Senior", "Lead"]

    def get_rung(self):
        return f"{self.__rung}"

    @classmethod
    def setRung(cls, new_rung):
        cls.__rung = new_rung
        cls.setBasicSalary(new_rung)

    @classmethod
    def setBasicSalary(cls, __rung):
        if __rung == cls.positions[0]:
            cls.salary = 1000
        elif __rung == cls.positions[1]:
            cls.salary = 2000
        elif __rung == cls.positions[2]:
            cls.salary = 3000
        elif __rung == cls.positions[3]:
            cls.salary = 5000
        else:
            cls.salary = 0

        # Junior = 1000
        # Middle = 2000
        # Senior = 3000
        # Lead = 5000


person1 = Person("Joe", "Black", 30)
person2 = Person.basedOnBYear("Kate", "Smith", 2000)
person3 = Person.basedOnStr("Kate Smith 25")
# # print(person1.getInfo())
# print(person1.getHi(input("Person, say\n")))
# print("ID:", person1.__get_id)

# print(person1._get_full_name())
#
# person1.change_age(25)
#
# print(person1.getInfo())

student1 = Student("Amogus", "Ne", 17, 100)

employee1 = Employee("Kate", "Smith", 25, "fucking HR", 2500, 7)

# print(student1.is_successful(9))

# person1.hobby = "shoot blacks joe"

# print(f"{person1.hobby}\n{person2.hobby}")

# print(person1.sayGreetings())

# print(employee1.get_sick_leave_perc())

# print(person3.getInfo())


Jun1 = Developer("Joe", "Black", 25, 20, "Back-End developer")
print(Jun1.get_rung())

Developer.setRung("Junior")
jun2 = Developer("Mick", "Black", 24, 50, "Full-stake developer")
print(jun2.get_rung(), "-", jun2.salary)


Developer.setRung("Senior")
jun3 = Developer("Mick", "Black", 24, 50, "Full-stake developer")
print(jun3.get_rung(), "-", jun3.salary)