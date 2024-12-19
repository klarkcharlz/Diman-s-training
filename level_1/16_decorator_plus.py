"""
Декоратор.
Декоратор функция, декорируем функцию и класс.
Декоратор класс.
Параметризированный декоратор.
wraps.
"""
from functools import wraps
import random

import test_import
print(help(test_import))


# декоратор частный случай замыкания
def deco(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("ЭТО ОБЕРТКА")
        res = func(*args, **kwargs)
        return res

    return wrapper


@deco
def summa(a: int, b: int) -> int:
    """Это функция суммирует 2 числа и возвращает результат.

    :param a: первое слагаемое
    :param b: второе слагаемое
    :return: результат сложения
    """
    return a + b


summa = deco(summa)


print(help(summa))

print(summa(1, 2))


def injection_age(cls):
    cls.age = 33
    return cls


@injection_age
class Human:
    pass


t = Human()
print(t.age)


class DecoClass:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("РАБОТАЕТ КЛАСС ДЕКОРАТОР ВСЕМ ЛЕЖАТЬ")
        res = self.func(*args, **kwargs)
        return res


@DecoClass
def raznost(a: int, b: int) -> int:
    return a - b


print(raznost(10, 2))


# deco_raznost = DecoClass(raznost)
# print(deco_raznost(22, 2))


# параметризированный декоратор
def params_deco(retries: int):

    def wrapper(func):

        def inner(*args, **kwargs):
            print("РАБОТАЕТ ПАРМЕТРИЗИРОВАННЫЙ ДЕКОРАТОР ВСЕМ СТОЯТЬ")
            for tries in range(retries + 1):
                try:
                    res = func(*args, **kwargs)
                except Exception as err:
                    print(f"Произошла ошибка: {err}")
                    if tries >= retries:
                        print("Превышено количество попыток!")
                        raise err
                else:
                    print(f"Получили результат с {tries + 1} попытки")
                    return res

        return inner

    return wrapper


# TODO Какой еще есть сахар в пайтоне, а есть ли соль?

@params_deco(3)
def random_div(number: int):
    res = number / random.randint(0, 3)
    return res


print(random_div(22))


# deco_random_div = params_deco(3)(random_div)
# print(deco_random_div(22))

# TODO ДОМАШНЕЕ ЗАДАНИЕ: КАК СДЕЛАТЬ ПАРАМЕТРИЗИРОВАННЫЙ ДЕКОРАТОР КЛАСС

def cash_deco(func):
    cash = {}

    def wrapper(*args, **kwargs):
        if args in cash:
            print(
                "С такими аргументами уже был вызов, не будем тратить время на вычисление, "
                "и вернем закешированное значение"
            )
            return cash[args]

        res = func(*args, **kwargs)
        cash[args] = res

        return res

    return wrapper


@cash_deco
def multiple(a: int, b: int):
    return a * b


print(multiple(1, 2))
print(multiple(3, 2))
print(multiple(4, 2))
print(multiple(1, 2))


def deco1(func):

    def wrapper(*args, **kwargs):
        print("Начал работу декоратор 1")
        res = func(*args, **kwargs)
        print("Закончил работу декоратор 1")
        return res

    return wrapper


def deco2(func):
    def wrapper(*args, **kwargs):
        print("Начал работу декоратор 2")
        res = func(*args, **kwargs)
        print("Закончил работу декоратор 2")
        return res

    return wrapper


def deco3(func):
    def wrapper(*args, **kwargs):
        print("Начал работу декоратор 3")
        res = func(*args, **kwargs)
        print("Закончил работу декоратор 3")
        return res

    return wrapper


@deco1
@deco2
@deco3
def test():
    pass


test()

# test_deco = deco1(deco2(deco3(test)))
# test_deco()
