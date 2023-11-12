from threading import Timer
import logging
from time import sleep


def worker(param):
    logging.info(param)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    one = Timer(1, worker, args=('one',))      # Timer використовується для відложеного запуску потоку,
    one.name = 'First thread'                         # наприклад при показу реклами відложено виводиться "закрити"
    one.start()

    two = Timer(2.5, worker, args=('two',))
    two.name = 'Second thread'
    two.start()

    sleep(2.51)                                      # якщо буде меньше чим вказано у Timer, то той Timer не запуститься

    one.cancel()
    two.cancel()
    logging.info('End program')