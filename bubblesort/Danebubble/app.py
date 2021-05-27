from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.Danebubble.Letters import alphabetize
from bubblesort.Danebubble.Numbers import order
from bubblesort.Danebubble.Words import order_length
bubblesort_Danebubble_bp = Blueprint('Danebubble', __name__,
                                      template_folder='templates',
                                      static_folder='static', static_url_path='assets')
bubblesort_Danebubblesort_bp = Blueprint('Danebubblesort', __name__,
                                          template_folder='templates',
                                          static_folder='static', static_url_path='assets')

@bubblesort_Danebubble_bp.route('/Dane_bubble')
def Danebubble():
    return render_template("Danebubble.html")

@bubblesort_Danebubblesort_bp.route("/", methods=["GET", "POST"])
def Danebubblesort():
    if request.method == 'POST':
        form = request.form
        return render_template("Danebubble.html", sorted_word=alphabetize(form["word"]), sorted_number=order(form["number"]), sorted_sentence=order_length(form["sentence"]))
    return redirect("/bubblesort/Danebubble")