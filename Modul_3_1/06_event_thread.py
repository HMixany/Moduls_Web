from threading import Thread, Event, current_thread
import logging
from time import sleep


def worker_timeout(event: Event, time: float):
    while not event.is_set():
        logging.info('Waiting for event to complete')
        e_wait = event.wait(timeout=time)     # True of False. Фактично це sleep(time)
        if e_wait:
            logging.info(f'Виконуємо роботу бо майстер наказав')
        else:
            logging.info(f'Можемо перепочити')


def worker(event: Event):
    logging.info(f'{current_thread().name} waiting')
    event.wait()
    logging.info(f'{current_thread().name} started')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    wrk = Thread(target=worker, args=(event,))
    wrk.start()

    wrk_timeout = Thread(target=worker_timeout, args=(event, 1))
    wrk_timeout.start()

    sleep(3)
    event.set()
    logging.info('End program')
