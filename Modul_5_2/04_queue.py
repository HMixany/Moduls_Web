import asyncio
from random import randint


async def producer(q: asyncio.Queue):
    num = randint(1, 1000)
    await asyncio.sleep(0.1)
    await q.put(num)                             # в чергу кладем рандомне число


async def consumer(q: asyncio.Queue):
    while True:
        num = await q.get()                      # дістаєм число з черги
        print(num ** 2)
        q.task_done()                            # обов'язково треба сказати в чергу, що роботу закінчили


async def main():
    queue = asyncio.Queue()
    consumer_tasks = [asyncio.create_task(consumer(queue)) for _ in range(3)]
    producer_tasks = [asyncio.create_task(producer(queue)) for _ in range(100)]
    await asyncio.gather(*producer_tasks)
    await queue.join()
    [task.cancel() for task in consumer_tasks]   # це не обов'язково, якщо далі в мейн немає асинхронних операцій


if __name__ == '__main__':
    asyncio.run(main())