from random import randint
from threading import Thread, RLock
import logging
from time import sleep


counter = 0
lock = RLock()


def worker():
    global counter
    while True:
        # lock.acquire()                       # теж саме що і with lock:
        with lock:                             # якщо не лочить потоки будуть спільний ресурс counter хаотично змінювати
            counter += 1
            sleep(randint(1, 3))
            logging.info(f'Counter: {counter}')
            with open('result.txt', 'a') as fh:
                fh.write(f'{counter}\n')
        # lock.release()                       # # теж саме що і with lock:


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.info('Start program')
    for i in range(10):
        t = Thread(target=worker, name=f'Thread#{i}')   # target приймає фунцію або функтор
        t.start()
    logging.info('End program')