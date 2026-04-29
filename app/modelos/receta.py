from modelos import db

# Tabla intermedia muchos a muchos
receta_ingrediente = db.Table('receta_ingrediente',
    db.Column('receta_id',      db.Integer, db.ForeignKey('receta.id'),      primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True),
    db.Column('cantidad',       db.Float,   nullable=False)
)


class Receta(db.Model):
    __tablename__ = 'receta'

    id          = db.Column(db.Integer, primary_key=True)
    nombre      = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    tiempo_min  = db.Column(db.Integer)
    dificultad  = db.Column(db.Enum('facil', 'medio', 'dificil'), default='facil')
    categoria   = db.Column(db.String(80))

    # Relaciones
    ingredientes = db.relationship('Ingrediente', secondary=receta_ingrediente, back_populates='recetas')

    def __repr__(self):
        return f'<Receta {self.nombre}>'


class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    id               = db.Column(db.Integer, primary_key=True)
    nombre           = db.Column(db.String(100), nullable=False)
    unidad           = db.Column(db.String(30))
    calorias_por_100g = db.Column(db.Float)

    # Relaciones
    recetas = db.relationship('Receta', secondary=receta_ingrediente, back_populates='ingredientes')

    def __repr__(self):
        return f'<Ingrediente {self.nombre}>'
