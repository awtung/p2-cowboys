from flask import Blueprint, render_template

chat_bp = Blueprint('chat', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')


@chat_bp.route('/')
def chat():
    return render_template("chat.html")