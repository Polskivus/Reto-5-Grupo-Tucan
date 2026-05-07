from flask import Blueprint, render_template, request, jsonify
import pymysql

nominas_aislada_bp = Blueprint('nominas_aislada', __name__)

def get_conn():
    return pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='Segura123',
        database='Gastro_basque',
        cursorclass=pymysql.cursors.DictCursor
    )

@nominas_aislada_bp.route('/')
def index():
    return render_template('Gestor_nominas.html')

@nominas_aislada_bp.route('/api/empleados', methods=['GET'])
def get_empleados():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    t.id            AS trabajador_id,
                    u.nombre        AS nombre,
                    c.id            AS contrato_id,
                    c.tipo          AS contrato,
                    c.salario_base  AS salario
                FROM trabajador t
                JOIN usuario  u ON u.id = t.usuario_id
                JOIN contrato c ON c.trabajador_id = t.id
                WHERE c.activo = TRUE
            """)
            rows = cur.fetchall()
        return jsonify(rows)
    finally:
        conn.close()

@nominas_aislada_bp.route('/api/empleados', methods=['POST'])
def add_empleado():
    data = request.json
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO usuario (nombre, email, password_hash, rol)
                VALUES (%s, %s, %s, 'trabajador')
            """, (data['nombre'], data['email'], 'temporal'))
            usuario_id = cur.lastrowid

            cur.execute("""
                INSERT INTO trabajador (usuario_id, cargo, departamento, fecha_alta)
                VALUES (%s, %s, %s, CURDATE())
            """, (usuario_id, data.get('cargo', 'Sin cargo'), data.get('departamento', '')))
            trabajador_id = cur.lastrowid

            cur.execute("""
                INSERT INTO contrato (trabajador_id, tipo, salario_base, fecha_inicio, activo)
                VALUES (%s, %s, %s, CURDATE(), TRUE)
            """, (trabajador_id, data['contrato'], data['salario']))

        conn.commit()
        return jsonify({'ok': True, 'trabajador_id': trabajador_id})
    finally:
        conn.close()

@nominas_aislada_bp.route('/api/empleados/<int:contrato_id>', methods=['PUT'])
def update_empleado(contrato_id):
    data = request.json
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE contrato
                SET tipo = %s, salario_base = %s
                WHERE id = %s
            """, (data['contrato'], data['salario'], contrato_id))

            cur.execute("""
                UPDATE usuario u
                JOIN trabajador t ON t.usuario_id = u.id
                JOIN contrato   c ON c.trabajador_id = t.id
                SET u.nombre = %s
                WHERE c.id = %s
            """, (data['nombre'], contrato_id))

        conn.commit()
        return jsonify({'ok': True})
    finally:
        conn.close()

@nominas_aislada_bp.route('/api/empleados/<int:contrato_id>', methods=['DELETE'])
def delete_empleado(contrato_id):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE contrato SET activo = FALSE WHERE id = %s", (contrato_id,))
        conn.commit()
        return jsonify({'ok': True})
    finally:
        conn.close()