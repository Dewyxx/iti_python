# Parent
class Shape:
    count = 0

    def __init__(self, _name, _color, _d1, _d2):
        self.name = _name
        self.color = _color
        self._d1 = _d1
        self._d2 = _d2
        Shape.count += 1

    def Area(self):
        return self._d1 * self._d2

    def __str__(self):
        return f"{self.name}, {self.color}, {self._d1}{self._d2}, {self.Area()}"

# Child
class Circle(Shape):
    count = 0

    def __init__(self, _radius, _color):
        super().__init__("Circle", _color, _radius, _radius)
        self.radius = _radius
        Circle.count += 1

    def Area(self):
        return 3.14* self.radius ** 2

# Objects
shape = Shape("Square", "Green", 5, 6)
print(f"Square Area = {shape.Area()}")
circle = Circle(3, "Blue")
print(f"Circle Area = {circle.Area()}")
print(Shape.count) 
