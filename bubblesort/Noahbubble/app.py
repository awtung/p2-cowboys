from flask import Blueprint, render_template, request
from bubblesort.Noahbubble.Noahbubble import NoahBubbleSort
bubblesort_Noahbubble_bp = Blueprint('Noahbubble', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@bubblesort_Noahbubble_bp.route('/Noahbubble', methods=["GET", "POST"])
def Noahbubble():
    if request.form:
        return render_template("Noahbubble.html", noahbubblesort=NoahBubbleSort(int(request.form.get("series"))))
    return render_template("Noahbubble.html", noahbubblesort=NoahBubbleSort("Start"))