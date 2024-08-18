from geometric_shapes import *

rectangle = Rectangle(10, 20)
ellipse = Ellipse(9, 7)
square = Square(4)
circle = Circle(20)
complex_shape = ComplexShape(circle, [rectangle, ellipse, square])
complex_shape_area = complex_shape.get_area()
complex_shape_edge_length = complex_shape.get_edge_length()