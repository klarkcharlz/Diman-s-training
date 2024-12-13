"""
Разница между is и ==. Как определить поведение == в своих классах.
"""


class Test:

    def __init__(self, a):
        self.a = a

    def __eq__(self, other: "Test"):
        if isinstance(other, self.__class__):
            return self.a == other.a
        if isinstance(other, int):
            return self.a == other


t1 = Test(1)
t2 = Test(2)
print(t1 == t2)
print(t1 == 1)


# is
print(t1 is t2)
print(id(t1) == id(t2))
