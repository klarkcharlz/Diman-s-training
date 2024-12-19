"""
Итераторы и генераторы.
Что это и в чем разница.
Как сделать свой итератор.
"""
from typing import Generator
# l = [1, 3, 4]
# for num in l:
#     print(num)


class Iterator:

    def __init__(self, array):
        self.array = array
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            elem = self.array[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return elem


for num in Iterator([1, 2, 3]):
    print(num)


iterator = Iterator([1, 2, 3])
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # StopIteration


range_s = iter(range(10))
print(next(range_s))
print(next(range_s))
print(next(range_s))


class IteratorA:

    def __init__(self, array):
        self.array = array
        self.index = 0

    def __next__(self):
        try:
            elem = self.array[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return elem


# без итера фор не работает TypeError: 'IteratorA' object is not iterable
# for num in IteratorA([1, 2, 3, 4]):
#     print(num)


class IteratorB:

    def __init__(self, array):
        self.array = array

    def __iter__(self):
        return IteratorA(self.array)


for num in IteratorB([5, 6, 7]):
    print(num)


i2 = IteratorB([5, 6, 7])
# print(next(i2))  # 'IteratorB' object is not an iterator
i2_iter = iter(i2)
print(next(i2_iter))


def generator() -> Generator[str, None, None]:  # Что за 3 аргумента ?
    for char in ["A", "B", "C"]:
        yield char
        print("sdfsdf")


gen = generator()
print(type(gen))
# for char in gen:
#     print(char)

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))


def balancing(queues: list):
    while True:
        for queue in queues:
            yield queue


balanc = balancing(["-", "+"])
print(balanc)
print(next(balanc))
print(next(balanc))
print(next(balanc))
print(next(balanc))
print(next(balanc))
print(next(balanc))
print(next(balanc))


def generator_send():
    value = yield "Начало"
    while True:
        value = yield f"Получено: {value}"


# TODO разберись сам с send или просто скажи на собеседование
#  что можно передавать данные в генератор через send


def custom_range(start, stop, step):
    while True:
        if start >= stop:
            return
        yield start
        start += step


cus_ran = custom_range(1, 10, 2)
for num in cus_ran:
    print(num)
