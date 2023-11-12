from threading import Thread


def worker(arg):
    print(arg)                                             # замість print в потоках треба використовувати logging


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = Thread(target=worker, args=(f'Count t - {i}',))   # target приймає фунцію або функтор
        t.start()
        threads.append(t)
    for t in threads:
        t.join()