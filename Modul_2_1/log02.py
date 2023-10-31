import logging
from my_logger import get_logger


logger = get_logger('my_logger', logging.DEBUG)


def baz(num: int):
    logger.info(f'Start function buz')
    foo_ = 100
    result = foo_ + num
    logger.debug(f'result = {result}')
    return result


def foo(num: int):
    logger.error("AAAAAAAAAAAAA!!!!!!!")


if __name__ == '__main__':
    baz(500)
    foo(500)