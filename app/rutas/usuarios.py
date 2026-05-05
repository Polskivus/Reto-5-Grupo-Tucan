from flask import Blueprint, render_template
from modelos.usuario import mostrar_usuarios

prueba_bp = Blueprint('prueba', __name__)

@prueba_bp.route('/prueba')
def listar_usuarios():
    usuarios = mostrar_usuarios()
    return render_template('prueba.html', usuarios=usuarios)