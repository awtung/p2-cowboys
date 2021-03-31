from flask import Blueprint, render_template, request
from MiniLabs.Noah.Noah import Factorial
MiniLabs_Noah_bp = Blueprint('Noah', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')

@MiniLabs_Noah_bp.route('/NoahLab', methods=["GET", "POST"])
def NoahLab():
    if request.form:
        return render_template("NoahLab.html", factorial=Factorial(int(request.form.get("series"))))
    return render_template("NoahLab.html", factorial=Factorial(2))