from flask import Blueprint, render_template

social_home_bp = Blueprint('aboutus', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@social_home_bp.route('/home')
def home():
    return render_template("homepage.html")

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

@social_home_bp.route('/Noah')
def Noahindividual():
    return render_template("noahindividual.html")

@social_home_bp.route('/Dane')
def Daneindividual():
    return render_template("daneindividual.html")

@social_home_bp.route('/Aiden')
def Aidenindividal():
    return render_template("aidenindividual.html")

@social_home_bp.route('/Nathan')
def Nathanindividal():
    return render_template("nathanindividual.html")

