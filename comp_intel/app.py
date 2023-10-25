import os

from flask import Flask, render_template, url_for, request, redirect, flash
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY


async def async_report(*args):
    """Создает отчет по чату телеграм."""
    pass


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


@app.route('/services', methods=['GET', 'POST'])
async def services():
    data = await async_report()

    channel = request.form.get('channel')
    check_users = request.form.get('users')
    check_messages = request.form.get('messages')

    if request.method == 'POST':

        if not(channel):
            flash('Заполните поле для проверки чата')
            return render_template('services.html', )

    else:
        flash('Для получения информации по группе заполните форму.')
    return render_template('services.html')


@app.route('/source')
def source():
    return render_template('source.html')


if __name__ == '__main__':
    app.debug = True
    app.run(debug=False, host='0.0.0.0')
