from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/training/<prof>')
def table(prof):
    return render_template("base.html", prof=prof)


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
