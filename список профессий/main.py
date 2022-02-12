from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

LIST = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, ' \
       'климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, ' \
       'метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')


@app.route('/list_prof/<lst>')
def index(lst):
    return render_template("base.html", lst_prof=LIST, tp=lst)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
