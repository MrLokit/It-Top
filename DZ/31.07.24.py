from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)

# Маршрут для страницы портфолио
@app.route('/')
def portfolio():
    people = Person.query.all()
    return render_template('portfolio.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)
