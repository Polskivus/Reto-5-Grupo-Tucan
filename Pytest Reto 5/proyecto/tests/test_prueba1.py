# test_prueba1.py
import pytest
from unittest.mock import patch, MagicMock
from src.prueba1 import conexion, recoge_nombre

def test_error1_conexion_puerto_incorrecto():
    """
    Error 1: El puerto 3306 es incorrecto.
    La conexión debe fallar y lanzar una excepción.
    """
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_connect.side_effect = Exception(
            "Can't connect to MySQL server: puerto incorrecto"
        )

        with pytest.raises(Exception) as excinfo:
            conexion()

        assert mock_connect.called, "Se debió intentar la conexión"
        assert "puerto" in str(excinfo.value).lower() or \
               "connect" in str(excinfo.value).lower()



def test_error2_parametro_execute_no_es_tupla():
    """
    Error 2: (usuario_comprobar) no es tupla, debe ser (usuario_comprobar,)
    Verificamos que el segundo argumento de execute NO es una tupla.
    """
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ("hash_falso",)
        mock_connect.return_value.cursor.return_value = mock_cursor

        recoge_nombre("admin")

        # Capturamos cómo se llamó execute
        args, kwargs = mock_cursor.execute.call_args

        # Este assert FALLA → documenta el bug (no es tupla)
        assert isinstance(args[1], tuple), \
            f"❌ Bug detectado: el parámetro es {type(args[1])}, debería ser tuple"


def test_error3_sin_manejo_de_none():
    """
    Error 3: Si fetchone() devuelve None, hacer None[0] lanza TypeError.
    La función debería manejar este caso pero no lo hace.
    """
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None  # Usuario no existe
        mock_connect.return_value.cursor.return_value = mock_cursor

        with pytest.raises(TypeError):
            recoge_nombre("usuario_que_no_existe")
