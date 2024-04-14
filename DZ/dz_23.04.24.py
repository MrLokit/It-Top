class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

irina = Person("Irina", 26)

print(f'{irina.name}\n{irina.age}\n') #Оригинал

irina.name = "Igor" # Изменение имени
irina.age = 31  # Изменение возраста
print(f'{irina.name}\n{irina.age}') #Измененное

del irina.name  # Удаление имени
del irina.age  # Удаление возраста