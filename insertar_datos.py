from app import create_app
from app.database import db
from app.models import Pelicula, Sesion
from datetime import date, time, timedelta, datetime

app = create_app()
app.app_context().push()

# Limpiar datos previos
Sesion.query.delete()
Pelicula.query.delete()
db.session.commit()

# Lista ampliada de películas
peliculas_data = [
    {"titulo": "Interstellar", "descripcion": "Viaje a través del espacio y el tiempo", "duracion": 169, "genero": "Ciencia ficción"},
    {"titulo": "Oppenheimer", "descripcion": "La historia del creador de la bomba atómica", "duracion": 180, "genero": "Biografía"},
    {"titulo": "Inception", "descripcion": "Sueños dentro de sueños", "duracion": 148, "genero": "Thriller"},
    {"titulo": "The Matrix", "descripcion": "Realidad simulada y lucha por la libertad", "duracion": 136, "genero": "Ciencia ficción"},
    {"titulo": "The Godfather", "descripcion": "La historia de una familia mafiosa", "duracion": 175, "genero": "Drama"},
    {"titulo": "Parasite", "descripcion": "Lucha de clases y secretos", "duracion": 132, "genero": "Thriller"},
    {"titulo": "Avengers: Endgame", "descripcion": "Superhéroes se unen para salvar el universo", "duracion": 181, "genero": "Acción"},
    {"titulo": "La La Land", "descripcion": "Historia de amor en Los Ángeles", "duracion": 128, "genero": "Musical"},
    {"titulo": "Joker", "descripcion": "Orígenes del villano Joker", "duracion": 122, "genero": "Drama"},
    {"titulo": "Frozen II", "descripcion": "Aventura congelada", "duracion": 103, "genero": "Animación"},
    {"titulo": "Dune", "descripcion": "La lucha por el control de un planeta desértico", "duracion": 155, "genero": "Ciencia ficción"},
    {"titulo": "The Dark Knight", "descripcion": "El caballero oscuro contra el Joker", "duracion": 152, "genero": "Acción"},
    {"titulo": "Titanic", "descripcion": "Romance en el fatídico viaje del Titanic", "duracion": 195, "genero": "Drama"},
]

# Crear objetos Pelicula
peliculas = []
for p in peliculas_data:
    pelicula = Pelicula(
        titulo=p["titulo"],
        descripcion=p["descripcion"],
        duracion=p["duracion"],
        genero=p["genero"]
    )
    peliculas.append(pelicula)

db.session.add_all(peliculas)
db.session.commit()

# Crear sesiones para cada película desde las 10:00 hasta las 23:00, cada 2 horas
sala_base = 1
for pelicula in peliculas:
    hora_actual = datetime.strptime("10:00", "%H:%M").time()
    hora_fin = datetime.strptime("23:00", "%H:%M").time()
    while hora_actual <= hora_fin:
        sesion = Sesion(
            id_pelicula=pelicula.id,
            fecha=date.today(),
            hora=hora_actual,
            sala=f"Sala {sala_base}"
        )
        db.session.add(sesion)

        # Incrementar 2 horas
        dt = (datetime.combine(date.today(), hora_actual) + timedelta(hours=2)).time()
        hora_actual = dt

    sala_base = (sala_base % 5) + 1  # Asigna salas de 1 a 5 en ciclo

db.session.commit()

print("Películas y sesiones ampliadas insertadas correctamente.")
