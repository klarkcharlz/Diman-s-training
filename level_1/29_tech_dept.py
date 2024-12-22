class LowMan(Exception):
    pass


class SuperMan:

    def __init__(self, power):
        if power == "low":
            raise LowMan
        self.power = power


try:
    ne_super = SuperMan("low")
except LowMan:
    print("ВНИМАНИЕ ОБНАРУЖЕН СЛАБЫЙ ЧЕЛОВЕК")


class NonFactoribleEnergySystem:

    def __init__(self, nums: int):
        self.nums = nums

    def __add__(self, other: int):
        self.nums += other
        return self


class MegaSuperProblemsInMyHouse:

    def __init__(self, nums: int):
        self.nums = nums

    def __add__(self, other: int):
        return self.__class__(self.nums + other)

    # TODO домашняя работа сделать все математические операции


izmen = NonFactoribleEnergySystem(33)
print(id(izmen))
izmen = izmen + 33
print(izmen.nums)
print(id(izmen))


ne_izmen = MegaSuperProblemsInMyHouse(33)
print(id(ne_izmen))
ne_izmen = ne_izmen + 33
print(ne_izmen.nums)
print(id(ne_izmen))


print(__name__)  # __main__


class Container:

    def __init__(self, collection):
        self.collection = collection

    def __len__(self):
        return len(self.collection)

    def __repr__(self):
        return f"{len(self)}"


box1 = Container([1, 2, 3])
box2 = Container([1, 2, 3, 2, 3])
box3 = Container([1, 2, 33, 2, 3, 44, 55])
print(len(box1))
boxes = [box3, box2, box1]
sort_boxes = sorted(boxes, key=len)
print(sort_boxes)
