from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_hashed_password_for_user(username):
    users = {
        'correct_username': bcrypt.generate_password_hash('correct_password')
    }
    return users.get(username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            message = 'Регистрация успешна!'
        else:
            message = 'Регистрация не удалась. Пожалуйста, заполните все поля.'
    return render_template('register.html', message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/news')
def news():
    if 'logged_in' in session:
        return render_template('newsAvtorisate.html')
    else:
        return redirect(url_for('login'))

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
