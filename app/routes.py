from flask import Blueprint, render_template

bp = Blueprint('index', __name__)


@bp.route('/')
@bp.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)
