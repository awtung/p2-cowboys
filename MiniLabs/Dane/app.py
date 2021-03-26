from flask import Blueprint, render_template

MiniLabs_Dane_bp = Blueprint('Dane', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Dane_bp.route('/')
def DaneLab():
    return render_template("DaneLab.html")