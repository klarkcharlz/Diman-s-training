"""
Шо такое GIL и зачем он нужен.

Эти штуки характерны и для асинхронности и процессов также:
Race condition
Deadlock
Lifelock

Потоки разделяют память между собой, процессы нет.
IO BOUND or CPU.

Потоки легче по ресурсам и быстрее создаются, чем процессы.
Процессы изолированы друг от друга, потоки — нет.
Создание пула потоков и процессов: ThreadPoolExecutor и ProcessPoolExecutor из concurrent.futures
"""

import threading
import time

# Вот это выучи
from threading import Lock, Semaphore, BoundedSemaphore, Event
from queue import Queue


def cpu_bound_task():
    total = 0
    for _ in range(10 ** 8):
        total += 1
    print(f"Сумма: {total}")


def main():
    threads = []
    start_time = time.time()

    for _ in range(3):
        thread = threading.Thread(target=cpu_bound_task, daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Время выполнения с потоками: {time.time() - start_time:.2f} сек")


if __name__ == "__main__":
    main()
