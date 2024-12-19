"""Разница между copy и deepcopy"""
from copy import deepcopy


def fill_list(array: list, num: int):
    array.append(num)


def fill_list2(array: list, num: int):
    array.append(num)
    return array


def increment_v1(num: int):
    num += 1


def increment_v2(num: int):
    num += 1
    return num


l = [1, 2, 3]
fill_list(l, 4)
print(l)  # [1, 2, 3, 4]

a = 33
increment_v1(a)
print(a)  # 33

a = increment_v2(a)
print(a)  # 34

print(id(l[2]))
l[2] += 1
print(l)
print(id(l[2]))

t = (1, 2, 3)
# t[1] += 1  # TypeError: 'tuple' object does not support item assignment

l2 = l.copy()  # копирует только не изменяемые типы
print(id(l) == id(l2))

ll1 = [1, 2, 3, [4]]
ll2 = ll1.copy()
print(id(ll1))
print(id(ll2))

print(id(ll1[3]))
print(id(ll2[3]))

ll2[3].append(1)

print(ll1[3])

ll3 = deepcopy(ll1)
print(id(ll1[3]))
print(id(ll3[3]))
