from flask import Flask
from config import Config
#import modelos.registro  # registra todos los modelos

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar blueprints (rutas)
    from rutas.recetas import recetas_bp
    from rutas.dietas  import dietas_bp
    from rutas.index import main_bp
    from rutas.nominas import nominas_bp
    from rutas.inicio_sesion import inicio_bp
    app.register_blueprint(inicio_bp)
    app.register_blueprint(nominas_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(recetas_bp)
    app.register_blueprint(dietas_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)