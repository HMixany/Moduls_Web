class Bird:
    def fly(self):
        return "I can fly"


class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly")