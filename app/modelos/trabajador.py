from modelos import db

class Trabajador(db.Model):
    __tablename__ = 'trabajador'

    id          = db.Column(db.Integer, primary_key=True)
    usuario_id  = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    cargo       = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100))
    fecha_alta  = db.Column(db.Date, nullable=False)

    # Relaciones
    usuario   = db.relationship('Usuario', back_populates='trabajador')
    contratos = db.relationship('Contrato', back_populates='trabajador')

    def __repr__(self):
        return f'<Trabajador {self.cargo}>'


class Contrato(db.Model):
    __tablename__ = 'contrato'

    id            = db.Column(db.Integer, primary_key=True)
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable=False)
    tipo          = db.Column(db.String(50), nullable=False)
    salario_base  = db.Column(db.Float, nullable=False)
    fecha_inicio  = db.Column(db.Date, nullable=False)
    fecha_fin     = db.Column(db.Date)
    activo        = db.Column(db.Boolean, default=True)

    # Relaciones
    trabajador = db.relationship('Trabajador', back_populates='contratos')
    nominas    = db.relationship('Nomina', back_populates='contrato')

    def __repr__(self):
        return f'<Contrato {self.tipo} - activo: {self.activo}>'


class Nomina(db.Model):
    __tablename__ = 'nomina'

    id            = db.Column(db.Integer, primary_key=True)
    contrato_id   = db.Column(db.Integer, db.ForeignKey('contrato.id'), nullable=False)
    periodo       = db.Column(db.Date, nullable=False)
    salario_bruto = db.Column(db.Float, nullable=False)
    deducciones   = db.Column(db.Float, nullable=False)
    salario_neto  = db.Column(db.Float, nullable=False)
    generada_en   = db.Column(db.DateTime, default=__import__('datetime').datetime.utcnow)

    # Relaciones
    contrato = db.relationship('Contrato', back_populates='nominas')

    def __repr__(self):
        return f'<Nomina {self.periodo} - neto: {self.salario_neto}>'
