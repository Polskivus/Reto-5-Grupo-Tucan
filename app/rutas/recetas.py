from flask import Blueprint, render_template
from modelos.receta import Receta

recetas_bp = Blueprint('recetas', __name__)

@recetas_bp.route('/recetas')
def index():
    recetas = Receta.query.all()
    return render_template('index.html', recetas=recetas)
