from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
