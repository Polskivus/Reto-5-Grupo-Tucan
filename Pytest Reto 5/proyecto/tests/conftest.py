# proyecto/tests/conftest.py
# Este archivo es "mágico" en pytest.
# Sirve para definir "fixtures" (datos o estados de configuración) 
# que cualquier prueba en la carpeta tests/ podrá usar
# automáticamente sin necesidad de importarlos.

import pytest

@pytest.fixture
def datos_suma():
    """Proporciona una tupla con datos de prueba estandarizados para sumar."""
    return (2, 3, 5) # a, b, resultado_esperado
