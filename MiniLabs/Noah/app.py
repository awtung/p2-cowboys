from flask import Blueprint, render_template

MiniLabs_Noah_bp = Blueprint('Noah', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')

@MiniLabs_Noah_bp.route('/')
def NoahLab():
    return render_template("NoahLab.html")