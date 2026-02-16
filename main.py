# flask --app main run
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def main_page():
    if request.method == 'POST':
        new_name = request.form['nazvanie']
        new_price = request.form['price']
        return render_template('index.html', 
                                user_new_name=new_name, 
                                user_new_price=new_price)
    return render_template('index.html')
    