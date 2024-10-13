import math
class Shape:
    def area(self):
        """Raises an error because this method should be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * self.radius ** 2
