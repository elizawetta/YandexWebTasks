from flask import Flask, render_template
from data import db_session
from data.users import User, Jobs
import datetime

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    for i in jobs:
        a = db_sess.query(User).filter(User.id == i.team_leader).first()
        i.team_leader = a.surname + " " + a.name

    return render_template("test.html", jobs=jobs)


def main():
    db_session.global_init("db/blogs.db")


if __name__ == '__main__':
    main()
    app.run(port=8000, host='localhost')
