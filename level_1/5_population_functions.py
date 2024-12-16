from functools import reduce, partial


# map
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)


def double_to_str(number: int):
    return str(number * 2)


def odd(number: int):
    return number % 2


str_numbers = list(map(double_to_str, numbers))
print(str_numbers)


# filter
odd_numbers = list(filter(odd, numbers))
print(odd_numbers)


# range
a = range(10)  # аргументы и факты
print(a)
list_a = list(a)
print(list_a)
for i in a:
    print(i)

print(list(range(10, 20, 2)))


# enumerate
for index, elem in enumerate(numbers):  # старт аргумент
    print(f"{index}) {elem}")

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in d:
    print(key)


for key in d.keys():
    print(key)


for values in d.values():
    print(values)


for key, value in d.items():
    print(f"{key}) {value}")


# sorted
trash_numbers = [2, 1, 5, 3, 1, 100, 0, -1000]
sorted_numbers = sorted(trash_numbers)
print(sorted_numbers)

# как сортируются строки


# редуцирующая функция reduce
def sum(a: int, b: int):
    return a + b


# [1, 2, 3, 4, 5, 6]
summa = reduce(sum, numbers, 1000)  # 2 или 3 аргумента
print(summa)


sum10 = partial(sum, 10)

print(sum10(20))
