import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Per(self):
        pass

    @abstractmethod
    def Sqr(self):
        pass

    @abstractmethod
    def Paint(self):
        pass

    @abstractmethod
    def Inf(self):
        pass

class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def Per(self):
        return self.side * 4

    def Sqr(self):
        return self.side ** 2

    def Paint(self):
        for i in range(self.side):
            print('*' * self.side)

    def Inf(self):
        sqr = self.Sqr()
        per = self.Per()
        print(f'''
===Квадрат===
Сторона: {self.side}
Цвет: {self.color}
Площадь: {sqr}
Периметр: {per}''')
        self.Paint()

class Rectangle(Shape):
    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

    def Per(self):
        return (self.width + self.height) * 2

    def Sqr(self):
        return self.width * self.height

    def Paint(self):
        for i in range(self.height):
            print('*' * self.width)

    def Inf(self):
        sqr = self.Sqr()
        per = self.Per()
        print(f'''
===Прямоугольник===
Длинна: {self.height}
Ширина: {self.width}
Цвет: {self.color}
Площадь: {sqr}
Периметр: {per}''')
        self.Paint()

class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def Per(self):
        return self.side1 + self.side2 + self.side3 # в примере вроде как неправильно вычислен этот периметр

    def Sqr(self):
        p = self.Per() / 2
        return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))

    def Paint(self):
        h = int(2 * self.Sqr() / self.side1)
        for i in range(h):
            print(' ' * (h - i - 1) + '*' * (2 * (i + 1) - 1))
    def Inf(self):
        sqr = self.Sqr()
        per = self.Per()
        print(f'''
===Треугольник===
Сторона 1: {self.side1}
Сторона 2: {self.side2}
Сторона 3: {self.side3}
Цвет: {self.color}
Площадь: {sqr:.2f}
Периметр: {per}''')
        self.Paint()

square = Square(3, 'red')
square.Inf()

rectangle = Rectangle(3, 7, 'green')
rectangle.Inf()

triangle = Triangle(11, 6, 6, 'yellow')
triangle.Inf()
