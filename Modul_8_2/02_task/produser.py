import json
from datetime import  datetime

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='web17 exchange', exchange_type='direct')    # створюємо біржу
channel.queue_declare(queue='web_17_queue', durable=True)    # durable=True збереже черги якщо перезапуститься контейнер
channel.queue_bind(exchange='web17 exchange', queue='web_17_queue')         # під'єднали бірржу до черги


def create_tasks(nums: int):
    for i in range(nums):
        message = {
            "id": i,
            "payload": f"Date: {datetime.now().isoformat()}"
        }

        channel.basic_publish(exchange='web17 exchange', routing_key='web_17_queue', body=json.dumps(message).encode())

    connection.close()                                                        # закрили


if __name__ == '__main__':
    create_tasks(100)