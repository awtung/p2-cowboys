#imports

from flask import Flask, render_template

#create "Flask"
app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template("homepage.html")

#about us
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

#run file
if __name__ == "__main__":
    app.run(debug = True)

