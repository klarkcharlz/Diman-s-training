"""
Дескрипторы и метаклассы.
"""


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # print(cls)
        # print(name)
        # print(bases)
        # print(dct)

        # print(f"Создание класса {name}")
        dct["method2"] = lambda self: print("Это метод2")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):

    def method1(self):
        pass
        # print("Это метод1")


obj = MyClass()
# obj.method2()


class Name:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Получение {self.name}")
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print(f"Установка {self.name} в {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Удаление {self.name}")
        instance.__dict__.pop(self.name, None)


class Person:
    name = Name("Diman")

    def __init__(self, name):
        self.name = name


diman = Person("Diman")
print(diman.name)
diman.name = "Nediman"
del diman.name
