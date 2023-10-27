from abc import ABC, abstractmethod


class Logger(ABC):                                # інтерфейс
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message):
        with open(self.file_name, 'w') as file:
            file.write(message)
