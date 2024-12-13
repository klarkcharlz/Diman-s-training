"""
Что может быть ключом словаря.
Хешируемый объект.
Как сделать свой хешируемый объект.
"""

# что может быть ключом словаря и почему

d = {
    "a": 33
}

d[1] = 22

print(d)


class Test:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{self.__class__.__name__}: {self.a}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.a}"

    # под капотом return id(self)
    def __hash__(self):
        return self.a

    # под капотом return id(self)
    def __eq__(self, other):
        return True


t1 = Test(1)
t2 = Test(1)

print(t1)

d[t1] = 12312321
d[t2] = 12312321
print(d)
print(d[t2])

# Коллизии и метод разрешения коллизий
