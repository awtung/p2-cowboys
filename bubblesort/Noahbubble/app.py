from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.Noahbubble.Noahbubble import BubbleSort
from bubblesort.Noahbubble.Noahwords import alphabetize
from bubblesort.Noahbubble.Noahnums import order
bubblesort_Noahbubblesort_bp = Blueprint('Noahbubblesort', __name__,
                                     template_folder='templates',
                                     static_folder='static', static_url_path='assets')
bubblesort_Noahsort_bp = Blueprint('Noahsort', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')

@bubblesort_Noahbubblesort_bp.route('/Noah_bubble', methods=["GET", "POST"])
def Noahbubblesort():
    if request.method == 'POST':
        form = request.form
        smallestNum = int(form["smallestNum"])
        largestNum = int(form["largestNum"])
        totalNum = int(form["totalNum"])
        return render_template("Noahbubble.html", bubblesort=BubbleSort(smallestNum, largestNum, totalNum))
    return render_template("Noahbubble.html", bubblesort=BubbleSort(0, 10, 5))

@bubblesort_Noahsort_bp.route('/Noah_sort', methods=["GET", "POST"])
def Noahsort():
    if request.method == 'POST':
        form = request.form
        return render_template("Noahbubble.html", word=alphabetize(form["words"]), num=order(form["nums"]))