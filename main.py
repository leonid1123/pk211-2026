from flask import Flask
from flask import render_template
from flask import request
import pymysql.cursors

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',
                       user='pk211',
                       password='1234',
                       database='pk211_db')
cur = conn.cursor()


def show_db():
    cur.execute('SELECT food_name, food_price FROM food_list')
    ans = cur.fetchall()
    food_lst = []
    for item in ans:
        food_lst.append(f"{item[0]}, {item[1]}р.")
    return food_lst


@app.route("/", methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        info = request.form.get('user_input')
        food_price = request.form.get('price')
        sql_txt = '''INSERT INTO food_list(food_name, food_price) 
        VALUES(%s, %s)'''
        new_values = (info, food_price)
        cur.execute(sql_txt, new_values)
        conn.commit()
        return render_template(
            'index.html',
            my_list=show_db())
    else:
        return render_template(
            'index.html',
                               my_list=show_db())


if __name__ == '__main__':
    app.run(debug=True)
