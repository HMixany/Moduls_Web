import sys
import os
import json
import time

import pika

from models import Task


def main():
    credentials = pika.PlainCredentials('jybbzliq', 'DIq5f0tk05MhcY-rjbzrk9rav-iL_lIY')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='hawk-01.rmq.cloudamqp.com', port=5672, credentials=credentials,
                                  virtual_host='jybbzliq'))
    channel = connection.channel()
    queue_name = 'web_17_campaign'
    channel.queue_declare(queue=queue_name, durable=True)

    consumer = "Mixany"

    def callback(ch, method, properties, body):
        pk = body.decode()
        task = Task.objects(id=pk, completed=False).first()
        if task:
            task.update(set__completed=True, set__consumer=consumer)
        # print(f" [x] Received {message}")
        # time.sleep(0.5)
        # print(f" [x] Completed {method.delivery_tag} task")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    # consume слухає і коли баче що щось прийщло, викликає callback

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
