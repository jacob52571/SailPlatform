import math

class GeometricShape:
    def __init__(self, name):
        self.set_name(name)
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

class Rectangle(GeometricShape):
    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.set_length(length)
        self.set_width(width)
    
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length
    
    def set_width(self, width):
        self.__width = width
    
    def get_perimeter(self):
        return 2 * self.get_length() + 2 * self.get_width()
    
    def get_area(self):
        return self.get_length() * self.get_width()
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        super().set_name("Square")
    
    def get_side(self):
        return super().get_length()
    
    def set_side(self, side):
        super().set_length(side)
        super().set_width(side)

class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.set_semi_major_axis(semi_major_axis)
        self.set_semi_minor_axis(semi_minor_axis)
        super().__init__('Ellipse')
    
    def get_semi_major_axis(self):
        return self.__semi_major_axis
    
    def get_semi_minor_axis(self):
        return self.__semi_minor_axis
    
    def set_semi_major_axis(self, semi_major_axis):
        self.__semi_major_axis = semi_major_axis
    
    def set_semi_minor_axis(self, semi_minor_axis):
        self.__semi_minor_axis = semi_minor_axis
    
    def get_perimeter(self):
        return math.pi * (3 * (self.get_semi_major_axis() + self.get_semi_minor_axis()) - math.sqrt((3 * self.get_semi_major_axis() + self.get_semi_minor_axis()) * (self.get_semi_major_axis() + 3 * self.get_semi_minor_axis())))

    def get_area(self):
        return math.pi * self.get_semi_major_axis() * self.get_semi_minor_axis()
    
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        super().set_name("Circle")
    
    def get_radius(self):
        return super().get_semi_major_axis()
    
    def set_radius(self, radius):
        super().set_semi_major_axis(radius)
        super().set_semi_minor_axis(radius)