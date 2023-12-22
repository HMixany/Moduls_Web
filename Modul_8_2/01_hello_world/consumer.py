import sys
import os

import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')           # підключиться до черги, якщо вона існує. Якщо не існу, то створе її

    """
    Функція callback повинна обов'язково приймати 4 аргументи:
    ch — поточний канал комунікації (цей об'єкт може перервати виконання циклу всередині start_consuming, якщо потрібно);
    method — детальна інформація про повідомлення;
    properties — службова інформація про повідомлення;
    body — тіло повідомлення у форматі bytes рядка.
    """
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
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
