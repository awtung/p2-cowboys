#imports

from flask import Flask, render_template
from social.home.app import social_home_bp

app = Flask(__name__)
app.register_blueprint(social_home_bp, url_prefix='/social/home')

@app.route('/')
def home():
    return "Hello"

#run file
if __name__ == "__main__":
    app.run(debug = True)

