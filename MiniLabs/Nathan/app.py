from flask import Blueprint, render_template, request
from MiniLabs.Nathan.Nathan import Sqrt
MiniLabs_Nathan_bp = Blueprint('Nathan', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Nathan_bp.route('/NathanLab', methods=["GET", "POST"])
def NathanLab():
    if request.form:
        return render_template("NathanLab.html", sqrt=Sqrt(int(request.form.get("series"))))
    return render_template("NathanLab.html", sqrt=Sqrt(4))