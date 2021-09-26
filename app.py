from flask import Flask, render_template, url_for, request, redirect   #render выводит страницы
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'       #Устанавливаем БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def index ():
    return render_template("index.html")


@app.route('/photos')
def photos ():
    return render_template("photos.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/report')
def report():
    return render_template("report.html")



@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)