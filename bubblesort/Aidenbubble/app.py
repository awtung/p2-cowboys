from flask import Flask, Blueprint, render_template, request, redirect

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
        userinput = form["Aidenbubble"]
        nums = list(map(int, userinput.split()))
        nums.sort()
        bubblesort = ", ".join(str(v) for v in nums)
        numbers = ", ".join(str(v) for v in userinput.split())
        return render_template("Aidenbubble.html", display=bubblesort, numbers=numbers)
    return redirect("/bubblesort/Noahbubble")