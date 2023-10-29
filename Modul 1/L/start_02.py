class Engine:
    def start(self):
        return 'Engine started'


class ElectricalEngine(Engine):
    def start(self):
        raise Exception('Starts differently')


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return f"Car started with {self.engine.start()}"


class ElectricCar(Car):
    def start(self):
        if isinstance(self.engine, ElectricalEngine):
            return f"Electric car: Electrical engine started with a button"
        else:
            return super().start()