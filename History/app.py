from flask import Blueprint, render_template, request
History_history_bp = Blueprint('History', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')

@History_history_bp.route('/')
def history():
    return render_template("history.html")