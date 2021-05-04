from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.Aidenbubble.bubble import Bubble


bubblesort_Aidenbubble_bp = Blueprint('Aidenbubble', __name__,
                                     template_folder='templates',
                                     static_folder='static', static_url_path='assets')
bubblesort_Aidenbubblesort_bp = Blueprint('Aidenbubblesort', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')

@bubblesort_Aidenbubble_bp.route('/Aidenbubble')
def Aidenbubble():
    return render_template("Aidenbubble.html")

@bubblesort_Aidenbubblesort_bp.route("/", methods=["GET", "POST"])
def Aidenbubblesort():
        if request.method == 'POST':
            form = request.form
            smallestNum = int(form["smallestNum"])
            largestNum = int(form["largestNum"])
            totalNum = int(form["totalNum"])
            # Check to make sure user input parameters are valid
            return render_template("Aidenbubble.html", bubble=Bubble(smallestNum, largestNum, totalNum))
        return redirect("/bubblesort/Aidenbubble")