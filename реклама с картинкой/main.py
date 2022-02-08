from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/promotion_image')
def index():
    return f"""<title>Колонизация</title>
    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    
    <h1>Жди нас, Марс!</h1>
    <img src="static/img/mars.png" width=300 height=300>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
    <div class="alert alert-primary" role="alert">Человечество вырастает из детства.</div>
    <div class="alert alert-secondary" role="alert">Человечеству мала одна планета.</div>
    <div class="alert alert-warning" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
    <div class="alert alert-danger" role="alert">И начнем с Марса!</div>
    <div class="alert alert-dark" role="alert">Присоединяйся!</div>
    """


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
