import pymysql

def conexion():
    conn = pymysql.connect(
    host='127.0.0.1',
    port=3307,
    user='root',
    password='Segura123',
    database='Gastro_basque',
    )
    return conn

def cerrar_conexion(conn):
    conn.close()

def recoge_nombre(usuario):
    conn = conexion()
    cursor = conn.cursor()

    usuario_comprobar = usuario

    sql_state_nombre = "SELECT password_hash from usuario where nombre = %s"
    cursor.execute(sql_state_nombre,(usuario_comprobar))

    usuario_bd_ps = cursor.fetchone()
    cerrar_conexion(conn)
    return usuario_bd_ps[0]