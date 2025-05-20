import math
import utils

class GeometricShape:
    def __init__(self, name):
        self.set_name(name)
    def get_name(self):
        return self.__name
    def set_name(self, name):
        utils.validate_non_empty_string(name)
        self.__name = name
    def __repr__(self):
        return f"GeometricShape(name={self.get_name()})"
    def __eq__(self, other):
        if isinstance(other, GeometricShape):
            return self.get_name() == other.get_name()
        return False

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
        utils.validate_positive_number(length)
        self.__length = length
    
    def set_width(self, width):
        utils.validate_positive_number(width)
        self.__width = width
    
    def get_perimeter(self):
        return 2 * self.get_length() + 2 * self.get_width()
    
    def get_area(self):
        return self.get_length() * self.get_width()
    
    def __repr__(self):
        return f"Rectangle(a={self.get_length()}, b={self.get_width()})"
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_length() == other.get_length() and self.get_width() == other.get_width()
        return False
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        super().set_name("Square")
    
    def get_side(self):
        return super().get_length()
    
    def set_side(self, side):
        super().set_length(side)
        super().set_width(side)

    def __repr__(self):
        return f"Square(a={self.get_side()})"
    
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.get_side() == other.get_side()
        return False

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
        utils.validate_positive_number(semi_major_axis)
        self.__semi_major_axis = semi_major_axis
    
    def set_semi_minor_axis(self, semi_minor_axis):
        utils.validate_positive_number(semi_minor_axis)
        self.__semi_minor_axis = semi_minor_axis
    
    def get_perimeter(self):
        return math.pi * (3 * (self.get_semi_major_axis() + self.get_semi_minor_axis()) - math.sqrt((3 * self.get_semi_major_axis() + self.get_semi_minor_axis()) * (self.get_semi_major_axis() + 3 * self.get_semi_minor_axis())))

    def get_area(self):
        return math.pi * self.get_semi_major_axis() * self.get_semi_minor_axis()
    
    def __repr__(self):
        return f"Ellipse(r1={self.get_semi_major_axis()}, r2={self.get_semi_minor_axis()})"
    
    def __eq__(self, other):
        if isinstance(other, Ellipse):
            return self.get_semi_major_axis() == other.get_semi_major_axis() and self.get_semi_minor_axis() == other.get_semi_minor_axis()
        return False
    
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        super().set_name("Circle")
    
    def get_radius(self):
        return super().get_semi_major_axis()
    
    def set_radius(self, radius):
        super().set_semi_major_axis(radius)
        super().set_semi_minor_axis(radius)

    def __repr__(self):
        return f"Circle(r={self.get_radius()})"
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_radius() == other.get_radius()
        return False

class ComplexShape(GeometricShape):
    def __init__(self, base, holes):
        super().__init__("ComplexShape")
        self.set_base(base)
        self.set_holes(holes)

    def get_base(self):
        return self.__base
    
    def get_holes(self):
        return self.__holes
    
    def set_base(self, base):
        self.__base = base
    
    def set_holes(self, holes):
        self.__holes = holes
    
    def add_hole(self, hole):
        l = self.get_holes()
        l.append(hole)
        self.set_holes(l)
    
    def remove_hole(self, hole):
        l = self.get_holes()
        l_new = []
        for h in l:
            if not h == hole:
                l_new.append(h)
        self.set_holes(l_new)
    
    def get_area(self):
        hole_areas = 0
        for hole in self.get_holes():
            hole_areas += hole.get_area()
        return self.get_base().get_area() - hole_areas
    
    def get_edge_length(self):
        hole_lengths = 0
        for hole in self.get_holes():
            hole_lengths += hole.get_perimeter()
        return self.get_base().get_perimeter() + hole_lengths
    
    def __repr__(self):
        return f"ComplexShape({self.get_base().get_name()} with {len(self.get_holes())} holes)"
