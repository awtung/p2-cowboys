#imports

from flask import Flask, render_template
from social.home.app import social_home_bp
from database.app import database_bp
from chat.app import chat_bp
from MiniLabs.Noah.app import MiniLabs_Noah_bp
from MiniLabs.Nathan.app import MiniLabs_Nathan_bp
from MiniLabs.Dane.app import MiniLabs_Dane_bp
from MiniLabs.Aiden.app import MiniLabs_Aiden_bp

app = Flask(__name__)
app.register_blueprint(social_home_bp, url_prefix='/aboutus')
app.register_blueprint(database_bp, url_prefix='/database')
app.register_blueprint(chat_bp, url_prefix='/chat')
app.register_blueprint(MiniLabs_Noah_bp, url_prefix='/MiniLabs/Noah')
app.register_blueprint(MiniLabs_Nathan_bp, url_prefix='/NathanLab')
app.register_blueprint(MiniLabs_Dane_bp, url_prefix='/DaneLab')
app.register_blueprint(MiniLabs_Aiden_bp, url_prefix='/MiniLabs/Aiden')


@app.route('/')
def home():
    return render_template("homepage.html")

#run file
if __name__ == "__main__":
    app.run(debug = True)

