import os

class Config:
    # Formato: mysql+pymysql://usuario:contraseña@host:puerto/nombre_bd
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:Segura123@127.0.0.1:3307/Gastro_basque'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'Contraseña_KLK')