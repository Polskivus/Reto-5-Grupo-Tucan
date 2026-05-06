import pytest
from app import create_app  # Asegúrate de importar create_app desde tu archivo principal

class TestApp:
    def app():
        app = create_app()
        app.config.update({
            "TESTING": True,
        })
        return app


    def client(app):
        """Crea un cliente de prueba para hacer peticiones."""
        return app.test_client()


    def test_app_is_created(app):
        assert app is not None
        assert app.name == 'app'  # O el nombre que tenga tu módulo principal

    # 2. Prueba de configuración: Verifica que la configuración se cargue
    def test_config(app):
        # Sustituye 'DEBUG' por una variable real de tu objeto Config
        # Esto asegura que la app esté leyendo tu archivo de configuración
        assert app.config['TESTING'] is True

    # 3. Prueba de Blueprints: Verifica que los blueprints estén registrados
    def test_blueprints_registered(app):
        # Lista de nombres esperados de tus blueprints
        expected_blueprints = [
            'inicio',  # Reemplaza con el nombre definido en Blueprint('nombre', ...)
            'prueba',
            'nominas',
            'main',
            'recetas',
            'dietas'
        ]
    
    # Comprobamos que las llaves de los blueprints registrados coincidan
    for bp in expected_blueprints:
        assert bp in app.blueprints