"""
Ехо-сервер: TCP протокол

Алгоритми роботи для сервера мережею, із встановленим з'єднанням, наступний:

Створюємо сокет типу socket.SOCK_STREAM
За допомогою методу bind зв'язуємо сокет із адресою служби
Запуск прослуховування запитів на створення з'єднання, метод listen
Повторюємо наступні дії у нескінченному циклі:
очікування запиту від клієнта створення з'єднання, метод accept
створення асинхронного потоку управління для обробки нового з'єднання
взаємодія з клієнтом у новому потоці через функцію handle за допомогою методів send та recv

Алгоритми роботи для клієнта:

Створюємо сокет типу socket.SOCK_STREAM
Встановлення з'єднання з сервером метод connect
Взаємодія з сервером за допомогою методів recv та send
Використання отриманих даних далі у програмі клієнта
"""
# Код клієнта:
import socket

TCP_IP = 'localhost'
TCP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        for line in MESSAGE.split(' '):
            print(f'Send data: {line}')
            sock.send(line.encode())
            response = sock.recv(1024)
            print(f'Response data: {response.decode()}')
    print(f'Data transfer completed')


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)