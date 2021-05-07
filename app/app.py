#imports

from flask import Flask, render_template
from social.home.app import social_home_bp
from database.app import database_bp
from chat.app import chat_bp
from MiniLabs.Noah.app import MiniLabs_Noah_bp
from MiniLabs.Nathan.app import MiniLabs_Nathan_bp
from MiniLabs.Dane.app import MiniLabs_Dane_bp
from MiniLabs.Aiden.app import MiniLabs_Aiden_bp
from bubblesort.Noahbubble.app import bubblesort_Noahbubblesort_bp
from bubblesort.Aidenbubble.app import bubblesort_Aidenbubblesort_bp
from bubblesort.Danebubble.app import bubblesort_Danebubble_bp
from bubblesort.Danebubble.app import bubblesort_Danebubblesort_bp

app = Flask(__name__)
app.register_blueprint(social_home_bp, url_prefix='/aboutus')
app.register_blueprint(database_bp, url_prefix='/database')
app.register_blueprint(chat_bp, url_prefix='/chat')
app.register_blueprint(MiniLabs_Noah_bp, url_prefix='/MiniLabs/Noah')
app.register_blueprint(MiniLabs_Nathan_bp, url_prefix='/MiniLabs/Nathan')
app.register_blueprint(MiniLabs_Dane_bp, url_prefix='/MiniLabs/Dane')
app.register_blueprint(MiniLabs_Aiden_bp, url_prefix='/MiniLabs/Aiden')
app.register_blueprint(bubblesort_Noahbubblesort_bp, url_prefix='/bubblesort/Noahbubble')
app.register_blueprint(bubblesort_Aidenbubblesort_bp, url_prefix='/bubblesort/Aidenbubble')
app.register_blueprint(bubblesort_Danebubble_bp, url_prefix='/bubblesort')
app.register_blueprint(bubblesort_Danebubblesort_bp, url_prefix='/Dane_bubble/')


@app.route('/')
def home():
    return render_template("homepage.html")

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

    quote = quote1 + " - " + random.choice(['Noah Pidding','Nathan Lee','Aiden Tung'])

    return render_template("randomapi.html", Title="Home", loginUsername='', logged_in=0, quote=quote)

#run file
if __name__ == "__main__":
     app.run(debug=True, port='5000', host='127.0.0.1')
    # app.run(debug=True, port='8080', host='192.168.1.5')

