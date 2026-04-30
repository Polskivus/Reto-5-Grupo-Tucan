from flask import Blueprint, render_template


nominas_bp = Blueprint('nominas', __name__)

@nominas_bp.route('/nominas')
def index():
    return render_template('Gestor_nominas.html')