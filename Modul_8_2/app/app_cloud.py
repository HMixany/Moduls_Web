import json
from datetime import datetime

import pika

from models import Task

credentials = pika.PlainCredentials('jybbzliq', 'DIq5f0tk05MhcY-rjbzrk9rav-iL_lIY')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='hawk-01.rmq.cloudamqp.com', port=5672, credentials=credentials,
                              virtual_host='jybbzliq'))
channel = connection.channel()

exchange = 'web17 Service'
queue_name = 'web_17_campaign'

channel.exchange_declare(exchange=exchange, exchange_type='direct')  # створюємо біржу
channel.queue_declare(queue=queue_name, durable=True)  # durable=True збереже черги якщо перезапуститься контейнер
channel.queue_bind(exchange=exchange, queue=queue_name)  # під'єднали бірржу до черги


def create_tasks(nums: int):
    for i in range(nums):
        task = Task(consumer="Noname").save()

        channel.basic_publish(exchange=exchange, routing_key=queue_name, body=str(task.id).encode(),
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    connection.close()  # закрили


if __name__ == '__main__':
    create_tasks(1)
