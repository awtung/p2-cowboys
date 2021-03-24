from flask import Blueprint, render_template

social_home_bp = Blueprint('social', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@social_home_bp.route('/')
def home():
    return render_template("homepage.html")



