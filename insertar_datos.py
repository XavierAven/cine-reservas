from app import create_app
from app.database import db
from app.models import Pelicula, Sesion
from datetime import date, time

app = create_app()
app.app_context().push()

# Elimina datos anteriores (opcional en desarrollo)
Sesion.query.delete()
Pelicula.query.delete()
db.session.commit()

# Crear películas
peliculas = [
    Pelicula(titulo="Interstellar", descripcion="Viaje a través del espacio y el tiempo", duracion=169, genero="Ciencia ficción"),
    Pelicula(titulo="Oppenheimer", descripcion="La historia del creador de la bomba atómica", duracion=180, genero="Biografía"),
    Pelicula(titulo="Inception", descripcion="Sueños dentro de sueños", duracion=148, genero="Thriller"),
    Pelicula(titulo="The Matrix", descripcion="Realidad simulada y lucha por la libertad", duracion=136, genero="Ciencia ficción"),
    Pelicula(titulo="The Godfather", descripcion="La historia de una familia mafiosa", duracion=175, genero="Drama"),
    Pelicula(titulo="Parasite", descripcion="Lucha de clases y secretos", duracion=132, genero="Thriller"),
    Pelicula(titulo="Avengers: Endgame", descripcion="Superhéroes se unen para salvar el universo", duracion=181, genero="Acción"),
    Pelicula(titulo="La La Land", descripcion="Historia de amor en Los Ángeles", duracion=128, genero="Musical"),
    Pelicula(titulo="Joker", descripcion="Orígenes del villano Joker", duracion=122, genero="Drama"),
    Pelicula(titulo="Frozen II", descripcion="Aventura congelada", duracion=103, genero="Animación")
]

db.session.add_all(peliculas)
db.session.commit()

# Crear sesiones para algunas películas
sesiones = [
    Sesion(id_pelicula=peliculas[0].id, fecha=date.today(), hora=time(17, 0), sala="Sala 1"),
    Sesion(id_pelicula=peliculas[0].id, fecha=date.today(), hora=time(20, 0), sala="Sala 2"),
    Sesion(id_pelicula=peliculas[1].id, fecha=date.today(), hora=time(18, 30), sala="Sala 1"),
    Sesion(id_pelicula=peliculas[2].id, fecha=date.today(), hora=time(19, 0), sala="Sala 3"),
    Sesion(id_pelicula=peliculas[3].id, fecha=date.today(), hora=time(21, 30), sala="Sala 1"),
    Sesion(id_pelicula=peliculas[4].id, fecha=date.today(), hora=time(16, 0), sala="Sala 4"),
    Sesion(id_pelicula=peliculas[5].id, fecha=date.today(), hora=time(18, 15), sala="Sala 2"),
    Sesion(id_pelicula=peliculas[6].id, fecha=date.today(), hora=time(20, 45), sala="Sala 3"),
    Sesion(id_pelicula=peliculas[7].id, fecha=date.today(), hora=time(17, 30), sala="Sala 1"),
    Sesion(id_pelicula=peliculas[8].id, fecha=date.today(), hora=time(19, 45), sala="Sala 4"),
    Sesion(id_pelicula=peliculas[9].id, fecha=date.today(), hora=time(15, 0), sala="Sala 5")
]

db.session.add_all(sesiones)
db.session.commit()

print("Películas y sesiones insertadas correctamente.")
