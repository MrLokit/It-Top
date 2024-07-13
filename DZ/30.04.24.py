import math as geometry

class Figure:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def area(self):
        print(f"Прямоугольник {self.color}. Площадь: ", end="")
        return self.__width * self.__height


rect = Rectangle(10, 20, "green")
rect.width = -10
print(rect.area())
