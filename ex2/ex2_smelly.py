from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    shape_type = 'circle'

    def __init__(self, **kwargs):
        self.radius = kwargs.get('radius')

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    shape_type = 'rectangle'

    def __init__(self, **kwargs):
        self.length = kwargs.get('length')
        self.width = kwargs.get('width')

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    shape_type = 'triangle'

    def __init__(self, **kwargs):
        self.base = kwargs.get('base')
        self.height = kwargs.get('height')

    def calculate_area(self):
        return 0.5 * self.base * self.height


class NullShape(Shape):
    def calculate_area(self):
        return None


def create_shape(shape_type, **kwargs):
    for shape_cls in (Circle, Rectangle, Triangle):
        if shape_cls.shape_type == shape_type:
            return shape_cls(**kwargs)
    return NullShape()
