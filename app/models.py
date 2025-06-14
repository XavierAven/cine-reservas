from .database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20), default='registrado')

class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(100))
    actores_principales = db.Column(db.String(200))

    sesiones = db.relationship('Sesion', backref='pelicula', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'duracion': self.duracion,
            'genero': self.genero,
            'director': self.director,
            'actores_principales': self.actores_principales
        }

class Sesion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pelicula = db.Column(db.Integer, db.ForeignKey('pelicula.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    sala = db.Column(db.String(50), nullable=False)

    asientos = db.relationship('Asiento', backref='sesion', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'hora': self.hora.strftime('%H:%M'),
            'sala': self.sala
        }

class Asiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_sesion = db.Column(db.Integer, db.ForeignKey('sesion.id'), nullable=False)
    numero_asiento = db.Column(db.String(10), nullable=False)
    reservado = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_sesion': self.id_sesion,
            'numero_asiento': self.numero_asiento,
            'reservado': self.reservado
        }

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_sesion = db.Column(db.Integer, db.ForeignKey('sesion.id'), nullable=False)
    asientos = db.Column(db.String(100), nullable=False)  # Lista o string de asientos reservados
    fecha_reserva = db.Column(db.DateTime, nullable=False)

class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_reserva = db.Column(db.Integer, db.ForeignKey('reserva.id'), nullable=False)
    metodo = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
