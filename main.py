from flask import Flask
from flask import render_template
from flask import request
import pymysql.cursors

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',
                       user='pk211',
                       password='1234',
                       database='pk211_db',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


@app.route("/", methods=['POST', 'GET'])
def main_page():
    user = request.form.get('login')
    login = request.form.get('password')
    if 'user_login' in request.form.keys():
        print('Вход пользователя')
    if 'guest_login' in request.form.keys():
        print('Вход гостя')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
