"""dir, __dict__, slots"""


class BlackMan:
    a = 33

    def __init__(self):
        self.b = 33
        self.aa = 44

    def bleaching(self):
        white = True
        print(locals())
        pass


black_man = BlackMan()
print(dir(black_man))

# TODO: ЧТО ТУТ ПРОИСХОДИТ
print(BlackMan.__dict__)
print(black_man.__dict__)
black_man.bleaching()
print(black_man.bleaching.__dict__)

black_man.__dict__["c"] = 23
print(black_man.c)


black_man.d = 33
black_man.sdfsdf = 13223
print(black_man.__dict__)


class WhiteMan:
    __slots__ = ["red", "man"]


wm = WhiteMan()
wm.red = "red"
wm.man = "man"
print(wm.red)
print(wm.man)
# print(wm.__dict__)  # 'WhiteMan' object has no attribute '__dict__'


# wm.age = 33  # 'WhiteMan' object has no attribute 'age'
