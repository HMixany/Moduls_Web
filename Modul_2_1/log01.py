import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(funcName)15s - %(message)s')

def baz(num: int):
    foo = 100
    result = foo + num
    logging.debug(f'result = {result}')
    return result


if __name__ == '__main__':
    baz(500)