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
# Код сервера:
import socket
from concurrent import futures as cf

TCP_IP = 'localhost'
TCP_PORT = 8080


def run_server(ip, port):
    def handle(sock: socket.socket, address: str):
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
            data = received.decode()
            print(f'Data received: {data}')
            sock.send(received)
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print(f'Start echo server {server_socket.getsockname()}')
    with cf.ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()
                client_pool.submit(handle, new_sock, address)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()
'''
У нашому коді робота сервера організована за принципом очікування підключення клієнта, а після отримання виконується 
зворотне пересилання повідомлень клієнту доти, доки він не закриє з'єднання
'''

if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)