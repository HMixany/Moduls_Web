"""
Щоб запустити "працівника", потрібно виконати в консолі таку команду:

celery -A mytasks worker --loglevel=INFO

Для Windows потрібно вказати додатковий параметр --pool solo.

celery -A mytasks worker --loglevel=INFO --pool solo
"""

from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


# відкладені задачі(таски)
@celery.task(name='Add two numbers')
def add(x, y):
    return x + y


@celery.task(name='Sub two numbers')
def sub(x, y):
    return x - y

