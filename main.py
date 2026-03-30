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


if __name__ == '__main__':
    app.run(debug=True)
