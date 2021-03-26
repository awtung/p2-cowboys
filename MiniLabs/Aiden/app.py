from flask import Blueprint, render_template

MiniLabs_Aiden_bp = Blueprint('Aiden', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Aiden_bp.route('/')
def AidenLab():
    return render_template("AidenLab.html")