from flask import Blueprint, render_template

social_home_bp = Blueprint('aboutus', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@social_home_bp.route('/')
def aboutus():
    return render_template("aboutus.html")

