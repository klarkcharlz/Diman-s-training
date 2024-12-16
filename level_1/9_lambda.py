"""лямбда функции. Что это и когда чаще всего применяются"""


def sum1(a: int, b: int) -> int:
    return a + b


print(sum1(2, 3))


sum2 = lambda a, b: a + b

l = [
    {"a": 1, "b": 3}, {"a": 33, "b": 222}, {"a": -1, "b": 45}, {"a": 13, "b": 23432}
]


def sorted_dict(d):
    return d["a"]


l = sorted(l, key=lambda d: d["b"])
# l = sorted(l, key=sorted_dict)
print(l)


l1 = [1, 2, 3, 33, 44]
l1 = list(filter(lambda number: number > 10, l1))
print(l1)
