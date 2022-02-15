from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder="templates")


@app.route('/login', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        return render_template("base.html")


if __name__ == '__main__':
    app.run(port=8000, host='localhost')
