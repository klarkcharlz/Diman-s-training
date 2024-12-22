"""
ООП
- атрибуты класса и экземпляра
- наследование
- супер
- селф
- проперти
- дандер методы
- класс метод и статик метод
- общее понятие наследование, полимофизм, инкапсуляция и абстракция
- защищенные и приватные методы
"""
import random


class Human:
    sex = "male"


h1 = Human()
h2 = Human()
h3 = Human()
print(h1.sex)  # берет атрибут класса
Human.sex = "female"
print(h1.sex)

h3.sex = "male"  # теперь это атрибут объекта, и он больше не берет значение у атрибута класса
print(h3.sex)
print(h1.sex)


class Animal:

    def __init__(self, legs: int):
        self.legs = legs


class Apple(Animal):

    def step(self):
        print(f"У меня {self.legs} ног")


class Page(Animal):

    def __init__(self, legs, sex):
        super().__init__(legs)
        self.sex = sex


apple = Apple(1)
page = Page(0, "male")


class Alice(Apple, Page):
    pass


alice = Alice(10, "cat")
alice.step()


print(Alice.__mro__)  # А что такое мро


# фикстуры
class Scan:

    def scan(self):
        print("Сканирую")


class Print:

    def print(self):
        print("Печатаю")


class Printer(Print):
    pass


class Scanner(Scan):
    pass


class MFU(Print, Scan):
    pass


class HardSoul:

    def __init__(self, angel, demon):
        self.demon = demon
        self.angel = angel
        self._black_angel = 0  # протектед
        self.__white_angel = 0  # приватный, _HardSoul__white_angel

    @property
    def power(self):
        return (self.angel + self.demon) * random.randint(1, 100_000)

    @property
    def white_angel(self):
        return self.__white_angel

    @white_angel.setter
    def white_angel(self, value):
        self.__white_angel = value


army = HardSoul(100, 20)
print(army.power)
print(army._black_angel)
# print(army.__white_angel)  # 'HardSoul' object has no attribute '__white_angel'
print(army._HardSoul__white_angel)
print(army.white_angel)
army.white_angel = 33
print(army.white_angel)


class EasyPeasy:

    def __init__(self, help):
        self.__help = help

    def set_help(self, value):
        self.__help = value

    def get_help(self):
        return self.__help

    def del_help(self):
        print("Удаляю ПОМОЩЬ!")

    help = property(get_help, set_help, del_help)


ep = EasyPeasy("HELP")
print(ep.help)
ep.help = 33
del ep.help


class Dunder:

    def __init__(self, num):
        self.num = num

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    def __getattr__(self, item):  # что делать если атрибут не найден
        print(f"Ищу: {item}")
        return 1

    # TODO вызывается при каждом обращение к атрибуту, ПОЧИНИ! ДЗ
    #   разберись сам:__getattribute__, __setattr__, __del__

    # TODO найти дандер методы для остальных сравнений

    def __call__(self, a):
        print("Я УМЕЮ ВЫЗЫВАТЬСЯ")


d1 = Dunder(33)
d2 = Dunder(22)
print(d1 > d2)
print(d1 < d2)
d1.num = 25

d1(33)  # вызываемый объект

print(d1.man)
print(d1.num)
print(d1.age)


class Back:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, a, b):
        self.a = a
        self.b = b


back = Back(1, b=33)


# полимофизм
def func(obj):
    obj.cry()

