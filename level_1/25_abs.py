"""
Абстрактные классы и интерфейсы
"""
from abc import ABC,  abstractmethod


class PrinterBase(ABC):

    def __init__(self, model: str, qr_code: str, color: str):
        self.model = model
        self.qr_code = qr_code
        self.color = color

    @abstractmethod
    def print(self):
        pass

    def clear(self):
        print("Протер салфеткой корпус!")

    def virtual(self, method):
        if method.__name__ in dir(self):
            print("Это виртуальный метод!!!! ВСЕМ ЛЕЖАТЬ")


class XeroxPrinter(PrinterBase):

    def print(self):
        print("КСЕРОКС ПЕЧАТАЕТ!!!")


xerox = XeroxPrinter("Xerox", "123", "Red")
xerox.print()
xerox.virtual(xerox.clear)


class PrinterInterface(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def virtual(self, method):
        pass


# class EbsonPrinter(PrinterInterface):
#     # нужно реализовать ВСЁ
