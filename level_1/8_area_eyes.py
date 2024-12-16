a = 123

l = [1, 2, 3]


def test(b: int):
    # если хочешь изменить глобальную неизменяемую переменную ее надо сюда запихнуть
    # или переопределить изменяемую
    global a
    # global l
    # l = [2, 3, 4]

    c = 123
    # не изменяемые глобальные переменные доступны только на чтение
    a += 1
    # l.append(22)

    # print(globals())  # Что тут выведет
    # print(locals())  # а тут

    return a + c


print(test(500))
print(l)


def test2():
    # шо такое
    print(a)  #  local variable 'a' referenced before assignment

    a = 123


# test2()


# Замыкания
# подготовь определение

def test4(c):  # 5
    d = 1

    def test5(e):
        # как в замыканиях изменять переменные из области видимости окружающей функции
        # nonlocal d
        # d += 1

        return c + d + e

    return test5


new_function = test4(5)
print(new_function(3))
