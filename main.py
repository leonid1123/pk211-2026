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


def show_db():
    cur.execute('SELECT food_name, food_price, id FROM food_list')
    ans = cur.fetchall()
    food_lst = []
    id_lst = []
    for item in ans:
        food_lst.append(f"{item['food_name']}, {item['food_price']}р.")
        id_lst.append(item['id'])
    return [food_lst, id_lst]


def total_sum():
    cur.execute('SELECT SUM(`food_price`) AS sum FROM `food_list` ')
    ans = cur.fetchone()
    return ans['sum']


@app.route("/", methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        info = request.form.get('user_input')
        food_price = request.form.get('price')
        if info and food_price:
            sql_txt = 'INSERT INTO food_list(food_name, food_price) VALUES(%s, %s)'
            new_values = (info, food_price)
            cur.execute(sql_txt, new_values)
            conn.commit()
            return render_template(
                'index.html',
                my_list=show_db()[0],
                info='Элемент добавлен',
                sum=total_sum(), btn_id=show_db()[1])
        else:
            return render_template('index.html',
                                   my_list=show_db()[0],
                                   info='Нужно заполнить все поля',
                                   sum=total_sum(),
                                   btn_id=show_db()[1])
    else:
        return render_template('index.html',
                               my_list=show_db()[0],
                               info='Добро пожаловать',
                               sum=total_sum(),
                               btn_id=show_db()[1])


@app.route("/<id>", methods=['GET'])
def del_item(name=None):
    print(name)
# разбор get запроса!!!

if __name__ == '__main__':
    app.run(debug=True)
