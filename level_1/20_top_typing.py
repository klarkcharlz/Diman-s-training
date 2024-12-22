"""Типизация"""
from typing import get_type_hints
from inspect import get_annotations


class Test:
    a: int
    b: str


print(Test.__annotations__)


def func(a: int, b: str, c: list, d):
    annotations = func.__annotations__
    print(annotations["a"])
    if not isinstance(a, annotations["a"]):
        raise ValueError("STOP")


print(func.__annotations__)
# print(dir(Test))

func(1, "2", [1, 2, 3], {1})


# TODO неужели они одинаковые ???
basic = get_type_hints(func)
print(basic)
vasic = get_annotations(func)
print(vasic)
