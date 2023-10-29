from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class GasEngine(Engine):
    def start(self):
        return "Gas engine started"


class ElectricalEngine(Engine):
    def start(self):
        return "Electrical engine started"


class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass
        return f"Car started with {self.engine.start()}"


class ElectricCar(Car):
    def start(self):
        return f'Electric car: {self.engine.start()}'


class GasCar(Car):
    def start(self):
        return f'Gas car: {self.engine.start()}'


gas_engine = GasEngine()
el_engine = ElectricalEngine()
mazda = GasCar(gas_engine)
tesla = ElectricCar(el_engine)
print(mazda.start())
print(tesla.start())