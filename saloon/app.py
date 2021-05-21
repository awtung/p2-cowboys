from flask import Blueprint, render_template, Flask,   request

app = Flask(__name__, static_folder = '/saloon/static')
saloon_saloon_bp = Blueprint('saloon', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')

@saloon_saloon_bp.route('/')
def saloon():
    return render_template("saloon.html")
