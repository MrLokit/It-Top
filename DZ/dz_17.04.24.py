def decor(func):
    def inner(*args, **kwargs):
        print("*" * 10, 'Данные автомобиля', "*" * 10)
        func(*args, **kwargs)
        print("=" * 40)
    return inner

class Auto:
    def __init__(self, model, year, madeby, power, color, price):
        self.model = model
        self.year = year
        self.madeby = madeby
        self.power = power
        self.color = color
        self.price = price

    def input_data (self):
        self.model = input('Название модели: ')
        self.year = input('Год выпуска: ')
        self.madeby = input('Производитель: ')
        self.power = input('Мощность двигателя: ')
        self.color = input('Цвет машины: ')
        self.price = input('Цена: ')
    @decor
    def display_data(self):
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.madeby)
        print("Мощность двигателя:", self.power)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)

auto1 = Auto('X7 M50i',
             2021,
             'BMW',
             '530 л.с.',
             'white',
             10790000)

auto1.display_data()
auto1.input_data()
auto1.display_data()