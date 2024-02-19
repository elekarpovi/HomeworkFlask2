# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти" При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input_form.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']

    response = make_response(redirect('/hello'))
    response.set_cookie('username', username)
    response.set_cookie('email', email)
    return response


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)