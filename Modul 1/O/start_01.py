from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator:                            # не соблюдається другий принцип SOLID. Якщо треба додати фігуру,
    def __init__(self, shapes: list[Rect]):      # прийдеться лізти у цей класс та додавати ще if у функцію total_area
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            if isinstance(el, Circle):
                sum += pi * el.radius ** 2
            if isinstance(el, Rect):
                sum += el.width * el.height
        return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Rect(4, 5), Circle(10), Rect(3, 3)]
    ac = AreaCalculator(shapes)
    print(ac.total_area())