from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def read(self):
        pass


class PDFBook(Book):
    def read(self):
        return 'Reading a PDF book...'


class EBookReader:
    def __init__(self, book: Book):
        self.book = book

    def read(self) -> str:
        return self.book.read()