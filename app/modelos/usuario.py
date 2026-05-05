import pymysql
from modelos.base_datos import cerrar_conexion, conexion

def mostrar_usuarios():
    conn = conexion()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM usuario")
    registro = cursor.fetchall()

    cerrar_conexion(conn)
    return registro