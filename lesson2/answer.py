from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pluto_is_planet_and_cuba_is_free'


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d = {'name': 'Mark', 'Surname': 'Watny', 'edu': 'Выше среднего', 'prof': 'штурман марсохода', 'sex': 'Male',
         'mot': 'Всегда мечтал застрять на Марсе!', 'ready': 'True'}
    return render_template('auto_answer.html', params=d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
