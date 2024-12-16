from collections import defaultdict, Counter, namedtuple
from statistics import mode
import itertools


# in
l = [1, 2, 3, 4, 5]
print(1 in l)
print(100 in l)

d = {
    "a": 33,
    "b": 22
}

print(22 in d.values())
print("a" in d.keys())


#  else в циклах
for i in range(10):
    if i == 3:
        break
    print(i)
else:
    print('бряков небыло')


i = 0
while i < 4:
    i += 1
    # if i == 3:
    #     break
    print(i)
else:
    print('бряков небыло')


# getattr / setattr
class Test:
    test = 33
    
    
class Test2(Test):
    pass


t = Test()
print(getattr(t, "test"))  # аналог c = t.test
print(f"{t.test}")

setattr(t, "age", 100)  # аналог t.test = 100
print(t.age)

for i in range(5):
    setattr(t, f"SuperValue{i}", 100)
print(dir(t))


for i in range(5):
    print(getattr(t, f"SuperValue{i}"))
    # print(t.SuperValue0)
    # print(t.SuperValue1)

# isinstance / issubclass
print(isinstance(t, Test))
print(issubclass(Test2, Test))

# defaultdict / Counter
# разделенный и объедененый словарь
d = {  # разделенный
    "a": 33,
    "b": 33
}
print(d["b"])

dd = defaultdict(int)  # объедененый
dd["a"] = 22
dd["b"] = 22

print(dd["c"])
print(dd["d"])

# c = int()
# print(c)

counter = Counter("s;odfhsdhf      usdhfuoids[foisd[ofhsdof")
print(counter)
print(counter.most_common()[0][0])

counter1 = Counter(list(range(10)) + list(range(5)) + list(range(3)))
print(counter1)

print(mode("s;odfhsdhf      usdhfuoids[foisd[ofhsdof"))


# zip
# zip который ориентируется на самую длинную коллекцую найди сам
for a, b, c in zip(
    ["a", "b", "c"],
    [1, 2, 3],
    [0.33, 3.33, 1.22, 123]
):
    print(f"{a} | {b} | {c}")


# Почитай про модуль рандом
import random
print(random.randint(22, 33))
print(random.choice([1, 3, 2]))
lll = [1, 3, 2]
random.shuffle(lll)
print(lll)

for a in itertools.chain(
    ["a", "b", "c"],
    [1, 2, 3],
    [0.33, 3.33, 1.22, 123]
):
    print(a)


def translate(string):
    return string.translate(string.maketrans("xy", "12"))


print(translate("ysdfsdfxsdfdsfy"))


# sum, min, max, all, any
print(sum([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))
print(max([1, 2, 3, 4]))

print(min(["1", "2", "3", "4"], key=lambda x: int(x)))

# print(list(map(lambda s: int(s), ["1", "2", "3", "4"])))
print(list(map(int, ["1", "2", "3", "4"])))


Coordinate = namedtuple(
    "Coordinate", "lat lon reference"
)
coordinate = Coordinate(11, 22, 33)
print(f"{coordinate=}")
print(coordinate[0])
print(coordinate.lon)
