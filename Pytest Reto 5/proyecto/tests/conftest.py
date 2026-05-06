# conftest.py
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_cursor():
    cursor = MagicMock()
    return cursor

@pytest.fixture
def mock_conexion(mock_cursor):
    with patch('src.prueba1.pymysql.connect') as mock_conn:
        mock_conn.return_value.cursor.return_value = mock_cursor
        yield mock_conn, mock_cursor
