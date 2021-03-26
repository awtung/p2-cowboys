from flask import Blueprint, render_template

MiniLabs_Nathan_bp = Blueprint('Nathan', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Nathan_bp.route('/')
def NathanLab():
    return render_template("NathanLab.html")