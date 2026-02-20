# flask --app main run
from flask import Flask
from flask import render_template
from flask import request
import random

app = Flask(__name__)

def get_random_int():
    return random.randrange(0,10)

AI_number = get_random_int()

@app.route("/", methods=['POST','GET'])
def main_page():
    global AI_number
    if request.method == 'POST':
        user_input = int(request.form['num'])
        if user_input > AI_number:
            txt = 'Чиселка очень большая'
        elif user_input < AI_number:
            txt = 'Чиселка очень маленькая'
        else:
            txt = 'Угадал!'
            AI_number = get_random_int()
        return render_template('index.html',ans = txt,old_value=user_input)

    return render_template('index.html', ans = 'пуп')
    