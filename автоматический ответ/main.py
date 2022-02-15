from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder="templates")
workers = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, ' \
          'климатолог, специалист по радиационной защите, астрогеолог, инженер жизнеобеспечения, ' \
          'оператор марсохода, киберинженер, пилот дронов, другое'.split(', ')


@app.route('/answer', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("answer.html")
    elif request.method == 'POST':
        d = dict()
        d['surname'] = request.form['surname']
        d['name'] = request.form['name']
        d['email'] = request.form['email']
        d['class'] = request.form['class']
        d['sex'] = request.form['sex']
        d['about'] = request.form['about']
        d['accept'] = request.form['accept']
        return render_template("auto_answer.html", **d)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
