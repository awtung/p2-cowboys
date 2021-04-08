# from flask import Blueprint, render_template, request
# from wtforms import IntegerField
# from flask_wtf import FlaskForm
# from wtforms.validators import InputRequired
# from flask_wtf.csrf import CSRFProtect
# from MiniLabs.Dane.Dane import get_area

# MiniLabs_Dane_bp = Blueprint('Dane', __name__,
#                              template_folder='templates',
#                              static_folder='static', static_url_path='assets')

# IMPORTANT - GENERATES CSRF TOKEN
# csrf = CSRFProtect(app)
# csrf.init_app(app)


# class RectangleForm(FlaskForm):
#    length = IntegerField('length', validators=[InputRequired()])
#    height = IntegerField('height', validators=[InputRequired()])


from flask import Blueprint, render_template, request
from MiniLabs.Dane.Dane import Power3
MiniLabs_Dane_bp = Blueprint('Dane', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

@MiniLabs_Dane_bp.route('/DaneLab', methods=["GET", "POST"])
def DaneLab():
    if request.form:

        return render_template("DaneLab.html", power3=Power3(int(request.form.get("series"))))
    return render_template("DaneLab.html", power3=Power3(3))
