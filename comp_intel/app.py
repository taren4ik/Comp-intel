import os
import datetime

from flask import Flask, render_template, url_for, request, redirect, flash
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY


@app.context_processor
def year():
    datetime_now = datetime.datetime.now()
    return {
        'year': datetime_now.year,
    }

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/report')
def report():
    return render_template('report.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.debug = True
    app.run(debug=False, host='0.0.0.0')
