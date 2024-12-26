"""
Asyncio, multithreading, multiprocessing
- определение для каждого
- когда что лучше использовать
- что такое GIL
- Какие механизмы синхронизации между потоками и корутинами знаете,
    как защитить какой то общий ресурс что бы он не изменялся сразу
    из нескольких потоков или процессов
- как передавать данные между процессами
- почему IO операции продолжают выполняться даже если работает другой поток

- евент луп
- сопрограмма
- корутина
- таска
- футура
- это один поток и один процесс
- это конкурентность
"""
from time import sleep
import asyncio


# синхронность
def sync_worker(name: str, lazy_timer: int):
    sleep(lazy_timer)
    print(f"Рабочий {name} приступил к работе через {lazy_timer} сек.")


workers = [
    ("Diman", 1),
    ("Nikolay", 10),
    ("Petr", 3)
]

# for name, lazy_timer in workers:
#     sync_worker(name, lazy_timer)


async def async_worker(name: str, lazy_timer: int):
    try:
        await asyncio.sleep(lazy_timer)  # запросы к бд, запросы в API, чтение
        print(f"Рабочий {name} приступил к работе через {lazy_timer} сек.")
    except asyncio.CancelledError:
        print("ОЙ ОЙ ОЙ МЕНЯ ОТМЕНИЛИ!")
        raise asyncio.CancelledError


async def main():
    # tasks = [
    #     asyncio.create_task(async_worker(name, lazy_timer))
    #     for name, lazy_timer in workers
    # ]
    # await asyncio.gather(*tasks)  # запустить пачку тасок/корутин разом
    coro = async_worker("name", 1)
    # await coro  # запускает корутину в работу
    # print(coro)
    task = asyncio.create_task(async_worker("name", 233))
    await asyncio.sleep(1)
    # print(task)
    task.cancel()
    await asyncio.sleep(3)
    print(task.cancelled())


# event_loop = asyncio.new_event_loop()
# asyncio.set_event_loop(event_loop)
# event_loop.run_until_complete(main())

asyncio.run(main())

# coro = async_worker("Hui", 123)
# print(coro)
