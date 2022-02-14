from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


# LIST = ["Ридли Скотт", "Энди Уир"]


@app.route('/distribution')
def index():
    return render_template("base.html", people=LIST)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
