from flask import Flask
from flask import render_template
from flask import request
import pymysql.cursors
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',
                       user='pk211',
                       password='1234',
                       database='pk211_db',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

UPLOAD_FOLDER = 'static/ing'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['POST', 'GET'])
def main_page():
    msg = ''
    if request.method == "POST":
        color = request.form.get('inp_color')
        size = request.form.get('inp_size')
        material = request.form.get("inp_material")

        img = request.files['inp_img']
        filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        sql = 'INSERT INTO t_shirt(color, size, material, img) VALUES(%s,%s,%s,%s)'
        ans = cur.execute(sql,(color,size,material,filename))
        conn.commit()
        if ans == 1:
            msg = 'Футболка добавлена'
        else:
            msg = 'Ошибка запроса'

    return render_template('index.html', msg=msg)


@app.route("/show", methods=['POST', 'GET'])
def show_all():
    params = None
    sql_filter = 'SELECT DISTINCT color from t_shirt'
    cur.execute(sql_filter)
    ans_filter = cur.fetchall()
    sql = 'SELECT * FROM t_shirt'
    if request.method == "POST":
        if 'sort_up' in request.form:
            sql = 'SELECT * FROM t_shirt ORDER BY size ASC'
        if 'sort_down' in request.form:
            sql = 'SELECT * FROM t_shirt ORDER BY size DESC'
        if 's_filter' in request.form:
            sql = 'SELECT * FROM t_shirt WHERE color=%s'
            filter_input = request.form.get('filter')
            params = filter_input
        if 'search' in request.form:
            search_input = request.form.get('search')
            search_input = '%'+search_input+'%'
            print('start:',search_input)
            sql = "SELECT * FROM t_shirt WHERE material LIKE %s"
            params = search_input

    cur.execute(sql, params)
    ans = cur.fetchall()
    return render_template('main_page.html',
                           all_list=ans,
                           ans_filter=ans_filter)


if __name__ == '__main__':
    app.run(debug=True)
