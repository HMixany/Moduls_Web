from threading import Thread, Event, current_thread
from time import sleep
import logging


def worker(event: Event):
    while True:
        if event.is_set():
            break
        sleep(1)
        logging.info(f'DDOS server')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()

    wrk = Thread(target=worker, args=(event,))
    wrk.start()

    sleep(5)
    event.set()
    logging.info('End program')