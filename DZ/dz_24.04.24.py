import  math

class Area:
    counter = 0

    @staticmethod
    def triangle_1(a, b, c):
        p = (a + b + c) / 2
        Area.counter += 1
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_2(a, h):
        Area.counter += 1
        return (a * h) / 2

    @staticmethod
    def square(a):
        Area.counter += 1
        return a ** 2

    @staticmethod
    def rectangle(a, b):
        Area.counter += 1
        return a * b

print(f'Площадь треугольника по формуле Герона: {Area.triangle_1(3, 4, 5)}')
print(f'Площадь треугольника через основание и высоту: {Area.triangle_2(6, 7)}')
print(f'Площадь квадрата: {Area.square(7)}')
print(f'Площадь прямоугольника: {Area.rectangle(2, 6)}')
print(f'Количество подсчетов площади: {Area.counter}')