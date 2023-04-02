"""Библиотека rectangle
- класс Rectangle с метожом get_area_rectangle считает площадь прямоуголника
- класс Square с методом get_area_sqare считает площад квадрата
"""

from rectangle import Rectangle, Square, Circle

"""Создаем объект класса прямоугольник Rectangle"""
rect_1 = Rectangle(3, 4)  # передаем значения 3, 4
rect_2 = Rectangle(12, 5)  # передаем значения 12, 5

"""Создаем объект класса квадрат Square"""
square_1 = Square(5)  # передаем значение 5
square_2 = Square(10)  # передаем значение 10

"""Создаем объект класса квадрат Circle"""
circle_1 = Circle(6)  # передаем значение (радиус) 6
circle_2 = Circle(13)  # передаем значение (радиус) 13

"""Создаем коллекцию список фигур"""
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]


"""Цикл на проверку с выводом на печать через функцию isinstance
является ли аргумент объекта экземпляром класса
 """
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_sqare())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area_rectangle())
