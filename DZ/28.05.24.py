class CountryCapitals:
    def __init__(self):
        self.data = {}

    def add_data(self, country, capital):
        self.data[country] = capital
        print('Файл сохранен')

    def delete_data(self, country):
        if country in self.data:
            del self.data[country]
            print('Данные удалены')
        else:
            print('Страна не найдена')

    def find_data(self, country):
        if country in self.data:
            print(f'({country}: {self.data[country]})')
        else:
            print('Страна не найдена')

    def edit_data(self, country, capital):
        if country in self.data:
            self.data[country] = capital
            print('Данные отредактированы')
        else:
            print('Страна не найдена')

    def display_data(self):
        for country, capital in self.data.items():
            print(f'({country}: {capital})')


country_capitals = CountryCapitals()

while True:
    print('''**********************************'
Выбор действия:
1- добавление данных
2- удаление данных
3- поиск данных
4- редактирование данных
5- просмотр данных
6- завершение работы''')
    choice = int(input('Ввод: '))

    if choice == 1:
        country = input('Введите название страны (с заглавной буквы): ')
        capital = input('Введите название столицы страны (с заглавной буквы): ')
        country_capitals.add_data(country, capital)
    elif choice == 2:
        country = input('Введите название страны для удаления: ')
        country_capitals.delete_data(country)
    elif choice == 3:
        country = input('Введите название страны для поиска: ')
        country_capitals.find_data(country)
    elif choice == 4:
        country = input('Введите название страны для редактирования: ')
        capital = input('Введите новое название столицы: ')
        country_capitals.edit_data(country, capital)
    elif choice == 5:
        country_capitals.display_data()
    elif choice == 6:
        break

