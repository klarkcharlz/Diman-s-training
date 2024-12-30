"""
ЧТО МОЖНО ПЕРЕДАВАТЬ МЕЖДУ ПРОЦЕССАМИ ?
"""
import multiprocessing
import time
import socket

import pickle  # ЕСЛИ ХОЧЕТСЯ ПРИМЕРОВ НАЙДИ САМ


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


QUEUE = multiprocessing.Queue()


class Test:
    pass


def gen():
    yield 1


a = gen()


def producer(queue):
    while True:
        time.sleep(3)
        # print(id(a))
        queue.put(a)


def consumer(queue):
    while True:
        food = queue.get(a)
        # print(id(food))
        # print(f"Consumer eat {food}")


if __name__ == "__main__":
    prod = multiprocessing.Process(target=producer, args=(QUEUE,), daemon=True)
    cons = multiprocessing.Process(target=consumer, args=(QUEUE,), daemon=True)

    prod.start()
    cons.start()

    prod.join()
    cons.join()
