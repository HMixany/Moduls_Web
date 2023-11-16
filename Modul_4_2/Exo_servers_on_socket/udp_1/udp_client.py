"""
Ехо-сервер: UDP протокол

Алгоритми роботи застосунків мережею, без встановленого з'єднання, наступний

Сервера:

Створюємо сокет типу socket.SOCK_DGRAM
За допомогою методу bind зв'язуємо сокет із адресою служби
Повторюємо наступні дії у нескінченному циклі:
запит у клієнта сокету даних методом recvfrom (блокуюча операція)
обробка даних
надсилання результату клієнту за допомогою методу sendto

Клієнта:

Створюємо сокет типу socket.SOCK_DGRAM
Надсилання повідомлення серверу методом sendto
Очікування відповіді від сервера за допомогою методу recvfrom
Використання отриманих даних далі у програмі клієнта
"""
# Код клієнта:
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    for line in MESSAGE.split(' '):
        data = line.encode()
        sock.sendto(data, server)
        print(f'Send data: {data.decode()} to server: {server}')
        response, address = sock.recvfrom(1024)
        print(f'Response data: {response.decode()} from address: {address}')
    sock.close()
"""
Наш приклад — звичайний ехо-сервер, який відправляє і отримує одні й ті самі дані на сервер. Сервер відкритий на порту 
8080 і отримує сокети даних у розмірі 1024 байт.
"""


if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)