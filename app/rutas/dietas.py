from flask import Blueprint, render_template

dietas_bp = Blueprint('dietas', __name__)

@dietas_bp.route('/dietas')
def index():
    return render_template('index.html')
