"""
crear_bd.py
-----------
Ejecuta este archivo UNA SOLA VEZ para crear todas las tablas.
Después ya no lo necesitas para nada.

"""
 
import pymysql
 
#Crear conexion para crear las tablas, solo ejecutar una vez para crear las tablas.
conn = pymysql.connect(
    host='127.0.0.1',
    port=3307,
    user='root',
    password='Segura123',
    database='Gastro_basque',
)
 
cursor = conn.cursor()
 
# Crear las tablas
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    nombre        VARCHAR(100)  NOT NULL,
    email         VARCHAR(150)  NOT NULL UNIQUE,
    password_hash VARCHAR(255)  NOT NULL,
    rol           ENUM('cliente', 'trabajador', 'admin') NOT NULL DEFAULT 'cliente',
    creado_en     DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS trabajador (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id   INT          NOT NULL,
    cargo        VARCHAR(100) NOT NULL,
    departamento VARCHAR(100),
    fecha_alta   DATE         NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS contrato (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    trabajador_id INT         NOT NULL,
    tipo          VARCHAR(50) NOT NULL,
    salario_base  FLOAT       NOT NULL,
    fecha_inicio  DATE        NOT NULL,
    fecha_fin     DATE,
    activo        BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (trabajador_id) REFERENCES trabajador(id)
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS nomina (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    contrato_id   INT      NOT NULL,
    periodo       DATE     NOT NULL,
    salario_bruto FLOAT    NOT NULL,
    deducciones   FLOAT    NOT NULL,
    salario_neto  FLOAT    NOT NULL,
    generada_en   DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contrato_id) REFERENCES contrato(id)
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS receta (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(150) NOT NULL,
    descripcion TEXT,
    tiempo_min  INT,
    dificultad  ENUM('facil', 'medio', 'dificil') DEFAULT 'facil',
    categoria   VARCHAR(80)
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingrediente (
    id                INT AUTO_INCREMENT PRIMARY KEY,
    nombre            VARCHAR(100) NOT NULL,
    unidad            VARCHAR(30),
    calorias_por_100g FLOAT
)
""")
 
# Tabla intermedia receta <-> ingrediente
cursor.execute("""
CREATE TABLE IF NOT EXISTS receta_ingrediente (
    receta_id      INT   NOT NULL,
    ingrediente_id INT   NOT NULL,
    cantidad_gramos       FLOAT NOT NULL,
    PRIMARY KEY (receta_id, ingrediente_id),
    FOREIGN KEY (receta_id)      REFERENCES receta(id),
    FOREIGN KEY (ingrediente_id) REFERENCES ingrediente(id)
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS dieta (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    nombre        VARCHAR(150) NOT NULL,
    descripcion   TEXT,
    tipo          VARCHAR(80),
    precio_mes    FLOAT        NOT NULL,
    duracion_dias INT
)
""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS suscripcion (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT  NOT NULL,
    dieta_id   INT  NOT NULL,
    inicio     DATE NOT NULL,
    fin        DATE,
    activa     BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (dieta_id)   REFERENCES dieta(id)
)
""")
 
# Confirmar los cambios y cerrar la conexion
conn.commit()
cursor.close()
conn.close()
 
print("Tablas creadas correctamente.")