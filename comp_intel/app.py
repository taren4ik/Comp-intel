from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)


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
    return render_template('services.html', )

    channel = request.form.get('channel')
    check_box = request.form.get('messages')
    check_box_users = request.form.get('users')
    print(check_box_users, check_box)
    if request.method == 'POST':
        if not (channel):
            flash('Заполните поле для проверки чата')

    else:
        flash('Для получения информации по группе заполните форму.')
    return render_template('services.html')




@app.route('/source')
def source():
    return render_template('source.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
