import asyncio

# Вот это выучи
from asyncio import Queue
from asyncio import Lock, Semaphore, BoundedSemaphore, Event


queue = asyncio.Queue()
lock = asyncio.Lock()  # мьютекс семафор


DATA = []


async def producer():
    while True:
        message = await queue.get()
        print(message)

        with lock:
            await asyncio.sleep(0.1)
            DATA.append(message)


async def consumer(name, number):
    while True:
        await asyncio.sleep(number)
        await queue.put(f"Привет от {name}")


async def main():
    producer_ = producer()
    consumer1 = consumer("Diman", 1)
    consumer2 = consumer("Kolan", 4)
    await asyncio.gather(producer_, consumer1, consumer2)


asyncio.run(main())
