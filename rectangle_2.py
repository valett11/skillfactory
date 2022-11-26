from rectangle import Rectangle, Square, Circle

rect1 = Rectangle(3, 5)
rect2 = Rectangle(4, 6)

# print(rect1.getArea())
# print(rect2.getArea())

square_1 = Square(5)
square_2 = Square(4)

# print(square_1.get_area_square())
# print(square_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(6)

figures = [rect1, rect2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print("Square Circle: ", figure.get_area_circle())
    else:
        print(figure.getArea())
