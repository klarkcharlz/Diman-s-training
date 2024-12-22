"""
- Изменяемый тип даннных как значенеи по умолчанию у аргумента функции
- Функция высшего порядка
- Сборщик мусора
- Мини-язык спецификации формата
    value = 123.456
    formatted_value = "{:.2f}".format(value)
    print(formatted_value)  # 123.46
- Monkey patch
- Инвариантность, Вариантность, Ковариантность, Контрвариантность
- атрибуты у функций
- датакласс
- компрехенсионс
"""
from dataclasses import dataclass
from enum import Enum
from dataclasses import dataclass


# для изменяемых типов данных в значениях по умолчанию создается ссылка
# один раз на моменте определения функции
def test(a=3, b=[]):  # так не надо
    b.append(a)
    return b


def test_right(a=3, b=None):  # а так можно
    b = b or []
    b.append(a)
    return b


l = [1, 2, 3]
l = test(4, l)
l = test(5, l)
l = test(6, l)

print(l)

l2 = test(7)
print(l2)
l3 = test(8)
print(l3)
l4 = test(9)
print(l4)

# TODO
# что такое функция Функция высшего порядка
# Сборщик мусора - 2 штуки garbage collector
# Monkey patch что это


class Test:

    def test(self):
        print("Тест")


def test_monkey(self):
    print("МАНКЕЙ ПАТЧ")


t = Test()
t.test()

Test.test = test_monkey
t1 = Test()
t1.test()

# А зачем и где такое может понадобиться?

# Инвариантность, Вариантность, Ковариантность, Контрвариантность

# Мини-язык спецификации формата
value = 123.456
formatted_value = f"{value:.2f}"
print(formatted_value)  # 123.46


def test1():
    count = getattr(test1, "count", 0)
    setattr(test1, "count", count + 1)
    print(f"Функция вызвана: {test1.count}")


test1()
test1.__call__()
test1.__call__()


def test2():
    pass


test2.count = 0
test2()
test2.count += 1
print(test2.count)


class Port(int, Enum):
    default_port = 5001
    port2 = 5001


# Почему он может быть полезен и когда его использовать?
# что есть полезного у датакласса
# Pydantic
@dataclass
class Settings:
    port: Port
    address: str


data = {
    "port": 5000,
    "address": "192.168.0.127"
}

settings = Settings(**data)
print(settings.port)


# компрехенсионс/comprehension/включения/генераторные выражения
l = [
    # "a" if not i % 4 else "b"
    i * j
    for i in range(10) for j in range(100)
    if not i % 2
]

d = {
    key: value
    for key, value in enumerate(range(5), start=20)
}

s = {num for num in range(10)}
print(s)
print(l)
print(d)

# ЭТО ГЕНЕРАТОР
gen = (num for num in range(10))
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
