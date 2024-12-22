"""
Паттерны:
- состояние
- шина данных
- прокси
- адаптер
- фабрика
- синглтон
"""


class Car:

    @classmethod
    def make_car(cls):
        return cls()


car = Car()
car2 = car.make_car()


class CarSharing:
    pass


class DeviceFabric:

    # def __init__(self, setting):
    #     self.setting = setting

    @staticmethod
    def make_cars(settings):
        return [Car() for _ in range(settings["num"])]

    @staticmethod
    def make_car_sharing(settings):
        return [CarSharing() for _ in range(settings.num)]


# fabrica = DeviceFabric({})
cars = DeviceFabric.make_cars({"num": 33})


def singletone(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        nonlocal instance

        if instance.get(cls):
            return instance[cls]
        else:
            instance[cls] = cls(*args, **kwargs)
            return instance

    return wrapper


@singletone
class NikolayPetrov:
    pass


np1 = NikolayPetrov()
np2 = NikolayPetrov()
np3 = NikolayPetrov()

print(id(np1))
print(id(np2))
print(id(np3))
