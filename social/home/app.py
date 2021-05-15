from flask import Blueprint, render_template

social_home_bp = Blueprint('aboutus', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@social_home_bp.route('/')
def aboutus():
    return render_template("aboutus.html")

@social_home_bp.route('/AidenTung')
def Aiden():
    return render_template("Aiden.html")

@social_home_bp.route('/NathanLee')
def Nathan():
    return render_template("Nathan.html")

@social_home_bp.route('/DaneVestal')
def Dane():
    return render_template("Dane.html")

@social_home_bp.route('/NoahPidding')
def Noah():
    return render_template("Noah.html")

@social_home_bp.route('/history')
def history():
    return render_template("history.html")