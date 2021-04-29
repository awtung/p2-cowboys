from flask import Flask, Blueprint, render_template, request, redirect
bubblesort_Noahbubble_bp = Blueprint('Noahbubble', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')
bubblesort_Noahbubblesort_bp = Blueprint('Noahbubblesort', __name__,
                                     template_folder='templates',
                                     static_folder='static', static_url_path='assets')

@bubblesort_Noahbubble_bp.route('/Noahbubble')
def Noahbubble():
    return render_template("Noahbubble.html")

@bubblesort_Noahbubblesort_bp.route("/", methods=["GET", "POST"])
def Noahbubblesort():
    if request.method == 'POST':
        form = request.form
        userinput = form["Noahbubble"]
        nums = list(map(int, userinput.split()))
        nums.sort()
        bubblesort = ", ".join(str(v) for v in nums)
        numbers = ", ".join(str(v) for v in userinput.split())
        return render_template("Noahbubble.html", display=bubblesort, numbers=numbers)
    return redirect("/bubblesort/Noahbubble")
