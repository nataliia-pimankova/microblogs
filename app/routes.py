from flask import Blueprint, render_template

from flask_login import login_required, current_user

from app.models import User

bp = Blueprint('index', __name__)


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = User.query.filter_by(username='natalya').first_or_404()
    posts = [
        {
            'author': User.query.filter_by(username='natalya').first(),
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': User.query.filter_by(username='susan').first(),
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)
