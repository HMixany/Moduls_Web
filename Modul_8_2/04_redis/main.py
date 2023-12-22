import pickle

import redis

client = redis.Redis(host='localhost', port=6379, password=None)


if __name__ == '__main__':
    client.set("username1", "Artem")
    client.set("username2", "Natalia")

    # У наших даних вічне існування. Змінемо для "username1" час існування на 600 сек
    client.expire("username1", 600)

    n = client.get("username2")
    print(n)                                # b'Natalia'

    client.set("test_list", pickle.dumps([2, 3, 4]))
    test_list = pickle.loads(client.get("test_list"))
    print(test_list)
