import pytest
from unittest.mock import patch, MagicMock
from src.prueba1 import conexion, recoge_nombre

def test_error1_conexion_puerto_incorrecto():
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_connect.side_effect = Exception("Can't connect to MySQL server: puerto incorrecto")
        with pytest.raises(Exception) as excinfo:
            conexion()
        assert mock_connect.called
        assert "puerto" in str(excinfo.value).lower() or "connect" in str(excinfo.value).lower()

def test_error2_parametro_execute_es_tupla():
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ("hash_falso",)
        mock_connect.return_value.cursor.return_value = mock_cursor
        recoge_nombre("admin")
        args, kwargs = mock_cursor.execute.call_args
        assert isinstance(args[1], tuple)

def test_error3_usuario_no_existe_devuelve_none():
    with patch('src.prueba1.pymysql.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_connect.return_value.cursor.return_value = mock_cursor
        resultado = recoge_nombre("usuario_que_no_existe")
        assert resultado is None
