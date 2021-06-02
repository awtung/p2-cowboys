#imports

from flask import Flask, render_template, request
from social.home.app import social_home_bp
from History.app import History_history_bp
from database.app import database_bp
from chat.app import chat_bp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String

from MiniLabs.Noah.app import MiniLabs_Noah_bp
from MiniLabs.Nathan.app import MiniLabs_Nathan_bp
from MiniLabs.Dane.app import MiniLabs_Dane_bp
from MiniLabs.Aiden.app import MiniLabs_Aiden_bp
from bubblesort.Noahbubble.app import bubblesort_Noahbubblesort_bp
from bubblesort.Aidenbubble.app import bubblesort_Aidenbubblesort_bp
from bubblesort.Nathanbubble.app import bubblesort_Nathanbubblesort_bp
from bubblesort.Danebubble.app import bubblesort_Danebubblesort_bp
from saloon.app import saloon_saloon_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.register_blueprint(social_home_bp, url_prefix='/aboutus')
app.register_blueprint(History_history_bp, url_prefix='/history')
app.register_blueprint(database_bp, url_prefix='/database')
app.register_blueprint(chat_bp, url_prefix='/chat')
app.register_blueprint(MiniLabs_Noah_bp, url_prefix='/MiniLabs/Noah')
app.register_blueprint(MiniLabs_Nathan_bp, url_prefix='/MiniLabs/Nathan')
app.register_blueprint(MiniLabs_Dane_bp, url_prefix='/MiniLabs/Dane')
app.register_blueprint(MiniLabs_Aiden_bp, url_prefix='/MiniLabs/Aiden')
app.register_blueprint(bubblesort_Noahbubblesort_bp, url_prefix='/bubblesort/Noahbubble')
app.register_blueprint(bubblesort_Aidenbubblesort_bp, url_prefix='/bubblesort/Aidenbubble')
app.register_blueprint(bubblesort_Nathanbubblesort_bp, url_prefix='/bubblesort/Nathanbubble')
app.register_blueprint(bubblesort_Danebubblesort_bp, url_prefix='/bubblesort/Danebubble/')
app.register_blueprint(saloon_saloon_bp, url_prefix='/saloon')


class Cowboy( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False)


@app.route('/')
def homenav():
    return render_template("homenav.html")


@app.route('/campfire', methods=["GET", "POST"])
def campfire():
    if request.method == 'POST':
        form = request.form
        name = form["Cowboy"]
        new_cowboy = Cowboy(name=name)
        db.session.add(new_cowboy)
        db.session.commit()
    results = db.session.query(Cowboy)
    return render_template("campfire.html", cowboys=results)


@app.route('/Clicker')
def clicker():
    return render_template("Clicker.html")


@app.route('/randomapi/', methods=['GET', 'POST'])
def quote():
    # call to random quote web api
    import requests
    import random

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
        'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #quote = response.text

    start1 = 'ent":'
    end1 = ',"ur'
    quote1 = response.text[response.text.find(start1)+len(start1):response.text.find(end1)+len(start1)-5]

    quote = quote1 + " - " + random.choice(['Noah Pidding','Nathan Lee','Aiden Tung', 'Dane Vestal'])

    return render_template("randomapi.html", Title="Home", loginUsername='', logged_in=0, quote=quote)

@app.route('/randomapi2/', methods=['GET', 'POST'])
def word():
    # call to random quote web api
    import requests

    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
        'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
        'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    start2 = 'rd":'
    end2 = '"pro'
    word2 = response.text[response.text.find(start2)+len(start2):response.text.find(end2)+len(start2)-5]

    word = word2



    return render_template("randomapi.html", Title="Home", loginUsername='', logged_in=0, word=word)

#run file
if __name__ == "__main__":
     db.create_all()
     app.run(debug=True, port='5000', host='127.0.0.1')
    # app.run(debug=True, port='8080', host='192.168.1.5')

