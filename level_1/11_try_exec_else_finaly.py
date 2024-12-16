"""try/except/else/finally"""

try:
    # 1 / 0
    1 / 2
except ZeroDivisionError:
    print("НЕ ДЕЛИ НА НОЛЬ")
else:
    print("А я поделил!")
finally:
    print("Пошел отдыхать")


def test():
    try:
        1 / 0
        return 1
    except ZeroDivisionError:
        # ....
        return 2
    else:
        return 3
    finally:
        # ...
        return 4


res = test()
print(res)
