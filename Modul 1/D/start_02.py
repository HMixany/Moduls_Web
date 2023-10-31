class PDFBook:
    def read(self):
        return 'Reading a PDF book...'


class EBookReader:
    def __init__(self):
        self.book = PDFBook()

    def read(self) -> str:
        return self.book.read()