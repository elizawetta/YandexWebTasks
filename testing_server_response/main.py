from flask import Flask, jsonify
from data.news_api import blueprint
from data import db_session
from flask import make_response

app = Flask(__name__)
app.register_blueprint(blueprint)
db_session.global_init("db/blogs.db")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()
