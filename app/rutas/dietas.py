from flask import Blueprint, render_template
from modelos.dieta import Dieta

dietas_bp = Blueprint('dietas', __name__)

@dietas_bp.route('/dietas')
def index():
    dietas = Dieta.query.all()
    return render_template('index.html', dietas=dietas)
