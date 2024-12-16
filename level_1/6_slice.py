"""Срезы. Что это и у каких объектов их можно брать."""

t = (1, 2, 3, 4, 5)
l = list(range(1000))
l1 = list(range(10))

d = {
    "a": 1,
    "b": 2,
    "c": 3
}


print(t[2:])
print(t[2:4])
print(l[1::100])

b = l[1::100]
print(b)
print(type(b))

# print(d[1:3])
print("sadassdasdasfdsdfsdfsd"[1:5])

# магия со срезами
print(l1)
del l1[2:5]
print(l1)

l1[2:4] = ["d", "e", "d", "e", "d", "e"]  # со строками не прокатит!!!
print(l1)

s = {1, 2, 3, 4}
# print(s[1:3])  # ПОЧЕМУ ОШИБКА!!!!
# print(s[1])

n = 3
b = 4
super_slice = slice(n, b)
print(super_slice)
print(type(super_slice))
print(l1[super_slice])
