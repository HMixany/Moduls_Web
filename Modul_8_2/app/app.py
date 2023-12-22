import json
from datetime import datetime

import pika

from models import Task

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

exchange = 'web17 Service'
queue_name = 'web_17_campaign'

channel.exchange_declare(exchange=exchange, exchange_type='direct')    # створюємо біржу
channel.queue_declare(queue=queue_name, durable=True)    # durable=True збереже черги якщо перезапуститься контейнер
channel.queue_bind(exchange=exchange, queue=queue_name)         # під'єднали бірржу до черги


def create_tasks(nums: int):
    for i in range(nums):
        task = Task(consumer="Noname").save()

        channel.basic_publish(exchange=exchange, routing_key=queue_name, body=str(task.id).encode())

    connection.close()                                                        # закрили


if __name__ == '__main__':
    create_tasks(100)
