from abc import ABC, abstractmethod


class MultiFunctionDevice(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class OldPrinter(MultiFunctionDevice):
    def print(self, document):
        # actual print logic
        pass

    def scan(self, document):
        raise Exception("OldPrinter don't scan")

    def fax(self, document):
        raise Exception("OldPrinter don't fax")