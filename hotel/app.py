from flask import Blueprint, render_template, request
Hotel_hotel_bp = Blueprint('Hotel', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')

@Hotel_hotel_bp.route('/')
def hotel():
    return render_template("hotel.html")

@Hotel_hotel_bp.route('/room1')
def room1():
    return render_template("room1.html")

@Hotel_hotel_bp.route('/room2')
def room2():
    return render_template("room2.html")

@Hotel_hotel_bp.route('/room3')
def room3():
    return render_template("room3.html")
