class Film:
    def __init__(self, title, genre, director, release_year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.duration = duration
        self.studio = studio
        self.actors = actors

class FilmController:
    def __init__(self):
        self.film_list = []

    def add_film(self, title, genre, director, release_year, duration, studio, actors):
        film = Film(title, genre, director, release_year, duration, studio, actors)
        self.film_list.append(film)

    def get_film_list(self):
        return self.film_list

    def find_film_by_title(self, title):
        for film in self.film_list:
            if film.title.lower() == title.lower():
                return film
        return None

    def delete_film(self, title):
        for film in self.film_list:
            if film.title.lower() == title.lower():
                self.film_list.remove(film)
                return True
        return False

class FilmView:
    def display_menu(self):
        print("===== Редактирование данных каталога фильмов =====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")

    def get_choice(self):
        return input("Выберите вариант действия: ")

    def display_film_added(self):
        print("=== Фильм добавлен ===")

    def display_film_catalog(self, film_list):
        print("=== Каталог фильмов ===")
        for index, film in enumerate(film_list, start=1):
            print(f"{index}: Фильм: {film.title}\nЖанр: {film.genre}\nРежиссер: {film.director}\nГод выпуска: {film.release_year}\nДлительность: {film.duration}\nСтудия: {film.studio}\nАктеры: {', '.join(film.actors)}\n")

    def display_film_information(self, film):
        print("=== Просмотр фильма ===")
        print(f"Название фильма: {film.title}\nЖанр: {film.genre}\nРежиссер: {film.director}\nГод выпуска: {film.release_year}\nДлительность: {film.duration}\nСтудия: {film.studio}\nАктеры: {', '.join(film.actors)}\n")

    def display_film_deleted(self):
        print("== Удалено ==")

    def display_exit_message(self):
        print("=== Вы вышли из программы ===")


if __name__ == "__main__":
    controller = FilmController()
    view = FilmView()

    while True:
        view.display_menu()
        choice = view.get_choice()

        if choice == "1":
            print('==================================')
            title = input("Название фильма: ")
            genre = input("Жанр: ")
            director = input("Режиссер: ")
            release_year = input("Год выпуска: ")
            duration = input("Длительность: ")
            studio = input("Студия: ")
            actors = input("Актеры (через запятую): ").split(", ")
            controller.add_film(title, genre, director, release_year, duration, studio, actors)
            view.display_film_added()

        elif choice == "2":
            films = controller.get_film_list()
            view.display_film_catalog(films)

        elif choice == "3":
            print('==================================')
            title = input("Введите название фильма для просмотра: ")
            film = controller.find_film_by_title(title)
            if film:
                view.display_film_information(film)
            else:
                print("Фильм не найден")

        elif choice == "4":
            print('==================================')
            title = input("Введите название фильма для удаления: ")
            deleted = controller.delete_film(title)
            if deleted:
                view.display_film_deleted()
            else:
                print("Фильм не найден")

        elif choice.lower() == "q":
            view.display_exit_message()
            break
