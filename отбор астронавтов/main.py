from flask import Flask, url_for, request

app = Flask(__name__)


def professions():
    workers = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, ' \
              'климатолог, специалист по радиационной защите, астрогеолог, инженер жизнеобеспечения, ' \
              'оператор марсохода, киберинженер, пилот дронов, другое'.split(', ')
    ans = ''
    for chel in workers:
        ans += f'''<div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                      <label class="form-check-label" for="flexCheckDefault">{chel.capitalize()}</label></div>\n'''
    return ans


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>

                            <h1 align=center>Анкета претендента</h1>
                            <h2 align=center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                    <p><div> <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email"></div></p>
                                    <p><div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div></p>
                                    <p><div class="form-group">
                                    <label for="form-check">Какие у Вас есть профессии?</label>
                                    {professions()}
                                    </div></p>
                                    <p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" >
                                          <label class="form-check-label" for="male"> Мужской</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female" checked>
                                          <label class="form-check-label" for="female">Женский</label>
                                        </div>
                                    </div>
                                    </p>
                                    <p>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите пронять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    </p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    </p>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "<h1 align=center>Форма отправлена</h1>"


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
