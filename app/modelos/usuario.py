from modelos import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id            = db.Column(db.Integer, primary_key=True)
    nombre        = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol           = db.Column(db.Enum('cliente', 'trabajador', 'admin'), nullable=False, default='cliente')
    creado_en     = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    trabajador   = db.relationship('Trabajador', back_populates='usuario', uselist=False)
    suscripciones = db.relationship('Suscripcion', back_populates='usuario')

    def __repr__(self):
        return f'<Usuario {self.email} - {self.rol}>'
