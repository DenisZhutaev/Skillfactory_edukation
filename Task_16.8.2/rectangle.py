class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area_rectangle(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def get_area_sqare(self):
        return self.a ** 2


class Circle:

    def __init__(self, a):
        self.a = a

    def get_area_circle(self):
        return 3.14 * self.a ** 2
