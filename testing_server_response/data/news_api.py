from flask import Blueprint, jsonify
from data import db_session
from data.users import Jobs

blueprint = Blueprint('blueprint', __name__, template_folder='templates')


@blueprint.route('/api/news')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify([item.to_dict() for item in jobs])


@blueprint.route('/api/news/<int:job_id>')
def get_one_news(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == job_id).all()
    if jobs:
        return jsonify([item.to_dict() for item in jobs])
    return jsonify({'error': 'Bad request'})
