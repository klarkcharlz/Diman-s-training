"""аггрегация и композиция в ООП"""


class Wheel:
    pass


class Engine:
    pass


class Car:

    def __init__(self):
        self.wheel = Wheel()
        self.engine = Engine()


class Student:
    pass


class University:

    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)


university = University()
student = Student()
university.add_student(student)
