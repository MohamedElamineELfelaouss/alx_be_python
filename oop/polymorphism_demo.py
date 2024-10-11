import math

# Base class
class Shape:
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle attributes."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle attributes."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * (self.radius ** 2)
