from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/table/<sex>/<age>')
def table(sex, age):
    age: str
    if age.isnumeric():
        return render_template("base.html", sex=sex, age=int(age))
    return '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
            <meta charset="UTF-8">
            <div class="alert-secondary"><h1 align="center">Миссия Колонизация Марса</h1></div>
            <div class="alert-light"><h4 align="center">И на Марсе будут яблони цвести!</h4></div>
            <div class="alert-danger"><h4 align="center">Ошибка</h4></div>'''


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
