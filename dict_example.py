from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main_page():
    h = 0
    fam = ''
    msg='Фамилия'
    if request.method == "POST":
        fam = request.form.get('s_name')
        if fam == '':
            msg = 'CЮда фамилию напиши!!!'
        x = request.form.get('mark1')
        y = request.form.get('mark2')
        z = request.form.get('mark3')
        if x.isnumeric() and y.isnumeric() and z.isnumeric():
            h = (int(x)+int(y)+int(z))/3
    return render_template('test.html', result=h, fam=fam, msg=msg)


app.run(debug=True)
