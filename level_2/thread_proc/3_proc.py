"""
Брокеры сообщений кто это и зачем
"""


import multiprocessing
import time

# Вот это выучи
from multiprocessing import Queue, Value, Manager, Pipe
from multiprocessing import Lock, Semaphore, BoundedSemaphore, Event


def cpu_bound_task():
    total = 0
    for _ in range(10 ** 8):
        total += 1
    print(f"Сумма: {total}")


def main():
    processes = []
    start_time = time.time()

    for _ in range(3):
        process = multiprocessing.Process(target=cpu_bound_task)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Время выполнения с процессами: {time.time() - start_time:.2f} сек")


if __name__ == "__main__":
    main()
