from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


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
    app.run(debug=False, host='0.0.0.0')
