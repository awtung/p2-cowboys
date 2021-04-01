from flask import Blueprint, render_template, request
from MiniLabs.Aiden.Aiden import Power2
MiniLabs_Aiden_bp = Blueprint('Aiden', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Aiden_bp.route('/AidenLab', methods=["GET", "POST"])
def AidenLab():
    if request.form:
        return render_template("AidenLab.html", power2=Power2(int(request.form.get("series"))))
    return render_template("AidenLab.html", power2=Power2(2))