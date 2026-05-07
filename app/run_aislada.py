#Creamos una "run" distinta, ya que queremos aislar 
#lo que es la parte del "trabajador" con lo que seria un usuario normal
#Aqui se ven las nominas, se pueden agregar, editar o eliminar.
from flask import Flask
from rutas.nominas_aislada import nominas_aislada_bp

app = Flask(__name__)
app.register_blueprint(nominas_aislada_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)