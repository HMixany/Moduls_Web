from math import pi


class Shape:
    def area_of(self):                  # не реалізований клас. Абстракція. Інтерфейс(наівнна реалізація)
        raise NotImplementedError()


class Rect(Shape):                      # наслідуємо інтерфейс
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):                   # обов'язково треба реалізувати метод
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area_of(self):
        return self.size ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return pi * self.radius ** 2


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for shape in self.shapes:
            sum += shape.area_of()
        return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Rect(4, 5), Circle(20), Square(3)]
    ac = AreaCalculator(shapes)
    print(ac.total_area())