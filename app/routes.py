from flask import Blueprint, render_template

from flask_login import login_required


bp = Blueprint('index', __name__)


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = {'username': 'Natalya'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)
