from flask import Blueprint, render_template, request
from wtforms import IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect
from MiniLabs.Dane.Dane import get_area

MiniLabs_Dane_bp = Blueprint('Dane', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')

# IMPORTANT - GENERATES CSRF TOKEN
# csrf = CSRFProtect(MiniLabs_Dane_bp)
# csrf.init_app(MiniLabs_Dane_bp)


class RectangleForm(FlaskForm):
    length = IntegerField('length', validators=[InputRequired()])
    height = IntegerField('height', validators=[InputRequired()])


@MiniLabs_Dane_bp.route('/DaneLab', methods=["GET", "POST"])
def DaneLab():
    form = RectangleForm()
    if request.form:
        length = form.length.data
        height = form.length.data
        area = get_area(length, height)
        return render_template("DaneLab.html", form=form, area=area)

