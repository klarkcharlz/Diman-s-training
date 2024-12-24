"""ЭТО ТЕСТОВЫЙ МОДУЛЬ"""
def retry(func):
    def wrapper(*args, **kwargs):
        print(func)
    return wrapper

def add_element(new: list[str] | str, src: list | None = None) -> list:
    if src is None:
        src=[]
    if isinstance(new, list):
        src.extend(new)
        print(id(src))
    else:
        src. append(new)
    return src
#
#
if __name__== "__main__":
    value1 = add_element("test")
    print(type(value1))
    value2 = add_element(["test2", "test3"])
    print(value2)
    value3 = add_element(["test4"], value2)




# def sum(a:int, b: int  | None = None ):
#
#     print(b is None)
#     print(b == None)
#     if b is None:
#         b=3
#     return a+b
# print(sum(4))


