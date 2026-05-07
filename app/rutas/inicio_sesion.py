from flask import Blueprint, render_template, request, session, redirect
from modelos.base_datos import recoge_nombre

inicio_bp = Blueprint('sesion', __name__)

@inicio_bp.route('/sesion', methods=['GET','POST'])

def check_sesion():
    if request.method == 'GET':
        return render_template('prueba.html')
    else:
        print("ENTRANDO EN CHECK_SESION")
        usuario = request.form['usuario']
        contra = request.form['contraseña']

        usuario_check = recoge_nombre(usuario)
        print(f"La contraseña llega? {usuario_check} y lo que le paso es {contra}")
        if contra == usuario_check:
            print("Sesion iniciada")
            session['usuario'] = usuario
            return render_template('index.html')
        else:
            print("Contraseña o usuario incorrecto")
            return render_template('prueba.html')
        
@inicio_bp.route('/CerrarSesion')

def cerrar_sesion():
    session.pop('usuario', None)
    return redirect('/')