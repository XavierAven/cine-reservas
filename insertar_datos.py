from app import create_app
from app.database import db
from app.models import Pelicula, Sesion, Usuario
from datetime import date, time
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

# Elimina datos anteriores (opcional en desarrollo)
Sesion.query.delete()
Pelicula.query.delete()
Usuario.query.delete()
db.session.commit()

# Crear usuario admin
admin = Usuario(
    nombre="Administrador",
    email="admin@cine.com",
    password=generate_password_hash("admin123"),
    tipo="admin"
)

db.session.add(admin)

# Crear películas
p1 = Pelicula(
    titulo="Interstellar",
    descripcion="Viaje a través del espacio y el tiempo",
    duracion=169,
    genero="Ciencia ficción"
)

p2 = Pelicula(
    titulo="Oppenheimer",
    descripcion="La historia del creador de la bomba atómica",
    duracion=180,
    genero="Biografía"
)

db.session.add_all([p1, p2])
db.session.commit()

# Crear sesiones
s1 = Sesion(id_pelicula=p1.id, fecha=date.today(), hora=time(17, 0), sala="Sala 1")
s2 = Sesion(id_pelicula=p1.id, fecha=date.today(), hora=time(20, 0), sala="Sala 2")
s3 = Sesion(id_pelicula=p2.id, fecha=date.today(), hora=time(18, 30), sala="Sala 1")

db.session.add_all([s1, s2, s3])
db.session.commit()

print("Películas, sesiones y usuario admin insertados correctamente.")
