"""
Брокеры сообщений кто это и зачем.
RabbitMQ и Apache Kafka.

Псевдокод:
бэк 1
rabbit.send(back2, [1, 2, 3,])
rabbit.get(back2)
"""


import multiprocessing
import time

# Вот это выучи
# FIFO LIFO КТО ТАКИЕ ???
from multiprocessing import Queue, Value, Manager, Pipe
from multiprocessing import Lock, Semaphore, BoundedSemaphore, Event

DATA = []


def cpu_bound_task():
    total = 0
    for _ in range(10 ** 8):
        total += 1
    print(f"Сумма: {total}")


def main():
    processes = []
    start_time = time.time()

    for _ in range(3):
        process = multiprocessing.Process(target=cpu_bound_task, daemon=True)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Время выполнения с процессами: {time.time() - start_time:.2f} сек")


if __name__ == "__main__":
    main()
