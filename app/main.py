from flask import Flask, render_template
from config import Config
from modelos import db
#import modelos.registro  # registra todos los modelos

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar SQLAlchemy
    db.init_app(app)

    # Crear tablas si no existen (útil en desarrollo)
    with app.app_context():
        import modelos.registro
        db.create_all()

    # Registrar blueprints (rutas)
    from rutas.recetas import recetas_bp
    from rutas.dietas  import dietas_bp
    app.register_blueprint(recetas_bp)
    app.register_blueprint(dietas_bp)

    # Ruta principal
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)