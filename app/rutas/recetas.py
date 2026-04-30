from flask import Blueprint, render_template

recetas_bp = Blueprint('recetas', __name__)

@recetas_bp.route('/recetas')
def index():
    return render_template('index.html')
