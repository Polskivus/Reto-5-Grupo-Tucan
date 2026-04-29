from modelos import db
from datetime import datetime

class Dieta(db.Model):
    __tablename__ = 'dieta'

    id            = db.Column(db.Integer, primary_key=True)
    nombre        = db.Column(db.String(150), nullable=False)
    descripcion   = db.Column(db.Text)
    tipo          = db.Column(db.String(80))
    precio_mes    = db.Column(db.Float, nullable=False)
    duracion_dias = db.Column(db.Integer)

    # Relaciones
    suscripciones = db.relationship('Suscripcion', back_populates='dieta')

    def __repr__(self):
        return f'<Dieta {self.nombre} - {self.precio_mes}€/mes>'


class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'

    id         = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    dieta_id   = db.Column(db.Integer, db.ForeignKey('dieta.id'),   nullable=False)
    inicio     = db.Column(db.Date, nullable=False)
    fin        = db.Column(db.Date)
    activa     = db.Column(db.Boolean, default=True)

    # Relaciones
    usuario = db.relationship('Usuario', back_populates='suscripciones')
    dieta   = db.relationship('Dieta',   back_populates='suscripciones')

    def __repr__(self):
        return f'<Suscripcion usuario:{self.usuario_id} dieta:{self.dieta_id}>'
