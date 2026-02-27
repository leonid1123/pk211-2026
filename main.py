from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

list_of_goods = []

@app.route("/", methods=['POST', 'GET'])
def main_page():
    info = request.form.get('user_input')
    list_of_goods.append(info)
    return render_template(
        'index.html',
        my_list=list_of_goods)


if __name__ == '__main__':
    app.run()
