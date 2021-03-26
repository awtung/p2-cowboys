from flask import Blueprint, render_template

database_bp = Blueprint('database', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')


@database_bp.route('/')
def database():
    return render_template("database.html")