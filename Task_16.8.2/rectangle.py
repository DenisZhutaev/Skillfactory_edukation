class Rectangle:
    """Класс прямоугольник
    Параметры:
    a (int or float): первая сторона прямоугольника
    b (int or float): вторая сторона прямоугольника
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area_rectangle(self):
        """Метод возвращвет площадь прямоугольника"""
        return self.a * self.b


class Square:
    """Класс квадрат
       Параметры:
       a (int or float): у квадрата все стороны равны
    """

    def __init__(self, a):
        self.a = a

    def get_area_sqare(self):
        """Метод возвращвет площадь квадрата"""
        return self.a ** 2


class Circle:
    """Класс квадрат
           Параметры:
           a (int or float): радиус круга
           число Пи (float): 3.14

    Формула нахождения площади круга: S=πR²
    """
    def __init__(self, a):
        self.a = a

    def get_area_circle(self):
        """Метод возвращвет площадь круга"""
        return 3.14 * self.a ** 2
