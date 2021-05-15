from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.Nathanbubble.Nathanbubble import BubbleSort

bubblesort_Nathanbubblesort_bp = Blueprint('Nathanbubblesort', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')

@bubblesort_Nathanbubblesort_bp.route('/Nathan_bubble', methods=["GET", "POST"])
def Nathanbubblesortbubblesort():
    if request.method == 'POST':
        form = request.form
        smallestNum = int(form["smallestNum"])
        largestNum = int(form["largestNum"])
        totalNum = int(form["totalNum"])
        return render_template("Nathanbubble.html", bubblesort=BubbleSort(smallestNum, largestNum, totalNum))
    return render_template("Nathanbubble.html", bubblesort=BubbleSort(0, 10, 5))

