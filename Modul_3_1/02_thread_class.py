from random import randint
from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.args = args
        self.counter = 0

    def run(self):                                # переопредилим метод run
        ttl = randint(1, 3)                 # формуємо затримку
        sleep(ttl)
        logging.info(f'In my thread {self.name}: {ttl} seconds passed')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    threads = []
    for i in range(10):
        t = MyThread(name=f"Thread#{i+1}", args=(f'Count t - {i}',))        # target немає т.к є метод run
        t.start()
        threads.append(t)
    [thr.join() for thr in threads]              # за допомогою цього програма чекає поки завешаться всі потоки
    # sleep(4)                                   # теж чекає, але повинна бути більше ttl
    logging.info('End program')