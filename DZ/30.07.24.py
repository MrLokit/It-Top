from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Контакты', 'url': 'contacts'},
        {'name': 'Об авторе', 'url': 'author'}
    ]
    return render_template('index.html', menu=menu, page_title='Главная')

@app.route('/news')
def news():
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Контакты', 'url': 'contacts'},
        {'name': 'Об авторе', 'url': 'author'}
    ]
    return render_template('news.html', menu=menu, page_title='Новости')

@app.route('/about')
def about():
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Контакты', 'url': 'contacts'},
        {'name': 'Об авторе', 'url': 'author'}
    ]
    return render_template('about.html', menu=menu, page_title='О нас')

@app.route('/contacts')
def contacts():
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Контакты', 'url': 'contacts'},
        {'name': 'Об авторе', 'url': 'author'}
    ]
    return render_template('contacts.html', menu=menu, page_title='Контакты')

@app.route('/author')
def author():
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'Новости', 'url': 'news'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Контакты', 'url': 'contacts'},
        {'name': 'Об авторе', 'url': 'author'}
    ]
    return render_template('author.html', menu=menu, page_title='Об авторе')

if __name__ == '__main__':
    app.run(debug=True)
