"""Исключения, что это, как обрабатывать, как создавать свои.
Иерархия исключений. Пустой raise.
Отлов нескольких исключений подряд и в одном блоке.
"""

# 1 / 0

try:
    1 / 0
except ZeroDivisionError as error:
    print(type(error))
    print(dir(error))
    # print(error.with_traceback())
    print(f"НЕ ДЕЛИ НА НОЛЬ!")


try:
    1 / 0
except:
    # шо эт такое
    pass


# l = [1, 2, 3, 4, 5]
# for num in l:
#     if num > 3:
#         raise RuntimeError("Stop")


try:
    1 / 0
except ZeroDivisionError:
    # зачем это надо
    print("Штото поделал выкидываю дальше")
    # raise


try:
    1 / 0
    l = [1, 2, 3]
    c = l[33]
except (ZeroDivisionError, IndexError):
    print("Это общий обработчик")


try:
    1 / 0
    l = [1, 2, 3]
    c = l[33]
except ZeroDivisionError:
    print("Это ZeroDivisionError обработчик")
except IndexError:
    print("Это IndexError обработчик")


# Выучить все исключения
# Выучить иерархию исключений, как отлавливаются дочерние и родительские исключения

