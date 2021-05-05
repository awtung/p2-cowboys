from flask import Blueprint, render_template, request, redirect
import numpy as np

bubblesort_Nathanbubble_bp = Blueprint('Nathanbubble', __name__,
                                       template_folder='templates',
                                       static_folder='static', static_url_path='assets')
bubblesort_Nathanbubblesort_bp = Blueprint('Nathanbubblesort', __name__,
                                           template_folder='templates',
                                           static_folder='static', static_url_path='assets')


@bubblesort_Nathanbubble_bp.route('/Nathanbubble')
def Nathanbubble():
    return render_template("Nathanbubble.html")


@bubblesort_Nathanbubblesort_bp.route("/", methods=["GET", "POST"])
def Nathanbubblesort():
    if request.method == 'POST':
        form = request.form
        smallestNum = int(form["smallestNum"])
        largestNum = int(form["largestNum"])
        # Check to make sure user input parameters are valid
        while smallestNum >= largestNum:
            print("Invalid number entered. Largest number must be greater than smallest number.")
            largestNum = int(input("Enter largest number: "))
        totalNum = int(form["totalNum"])
        # Generate random array based on user input
        array = np.random.randint(smallestNum, largestNum, totalNum)
        original = ", ".join(str(v) for v in array)
        # Traverse through all array arrays
        for i in range(totalNum - 1):
            # Traverse the array from 0 to n-i-1
            for j in range(0, totalNum - i - 1):
                # Swap if the array found is greater
                # than the next array
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        bubblesort = ", ".join(str(v) for v in array)
        # Driver code to test above
        # bubbleSort()
        return render_template("Nathanbubble.html", display=bubblesort, original=original)
    return redirect("/bubblesort/Nathanbubble")
