# Importa todos los modelos aquí para que SQLAlchemy los registre
# al llamar db.create_all() en main.py
from modelos.usuario    import Usuario
from modelos.trabajador import Trabajador, Contrato, Nomina
from modelos.receta     import Receta, Ingrediente
from modelos.dieta      import Dieta, Suscripcion
