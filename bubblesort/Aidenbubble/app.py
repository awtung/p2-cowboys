from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.Aidenbubble.Aidenbubble import BubbleSort
from bubblesort.Aidenbubble.Aidenwords import alphabetize
from bubblesort.Aidenbubble.Aidennums import order
bubblesort_Aidenbubblesort_bp = Blueprint('Aidenbubblesort', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')


@bubblesort_Aidenbubblesort_bp.route('/Aiden_bubble', methods=["GET", "POST"])
def Aidenbubblesort():
    if request.method == 'POST':
        form = request.form
        smallestNum = int(form["smallestNum"])
        largestNum = int(form["largestNum"])
        totalNum = int(form["totalNum"])
        return render_template("Aidenbubble.html", bubblesort=BubbleSort(smallestNum, largestNum, totalNum), word=alphabetize(form["words"]), num=order(form["nums"]))
    return render_template("Aidenbubble.html", bubblesort=BubbleSort(0, 10, 5))






