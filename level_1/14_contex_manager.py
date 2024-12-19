"""Контекстный менеджер, что это, как сделать свой. with"""

file = open('./test.txt', 'r', encoding='utf-8')
data = file.read()
file.close()


with open('./test.txt', 'r', encoding='utf-8') as file:
    data = file.read()


class Open:

    def __init__(self, path: str):
        self.path = path
        self.file = None

    def __enter__(self):
        self.file = open(self.path, 'r', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.file.close()


with Open('./test.txt') as file:
    data = file.read()
    # 1 / 0
    print(data)


class Dummy:
    def __enter__(self):
        print("что предварительно сделал")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Чтото сделал после")


with Dummy():
    a = 33
    a += 1
