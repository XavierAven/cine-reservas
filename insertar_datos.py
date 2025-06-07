from app import create_app, db
from app.models import Pelicula, Sesion
from datetime import date, time

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    peliculas = [
        Pelicula(
            titulo="Interstellar",
            descripcion="Un grupo de exploradores viaja a través de un agujero de gusano en el espacio en un intento por asegurar el futuro de la humanidad.",
            duracion=169,
            genero="Ciencia ficción",
            director="Christopher Nolan",
            actores_principales="Matthew McConaughey, Anne Hathaway, Jessica Chastain"
        ),
        Pelicula(
            titulo="El Padrino",
            descripcion="La historia de la familia mafiosa Corleone en Estados Unidos tras la Segunda Guerra Mundial.",
            duracion=175,
            genero="Drama",
            director="Francis Ford Coppola",
            actores_principales="Marlon Brando, Al Pacino, James Caan"
        ),
        Pelicula(
            titulo="Inception",
            descripcion="Un ladrón experto en el arte de robar secretos del subconsciente recibe la tarea de implantar una idea en la mente de un objetivo.",
            duracion=148,
            genero="Thriller",
            director="Christopher Nolan",
            actores_principales="Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page"
        ),
        Pelicula(
            titulo="Parasite",
            descripcion="Una familia pobre se infiltra en la vida de una familia rica en un juego de engaños con consecuencias inesperadas.",
            duracion=132,
            genero="Thriller",
            director="Bong Joon-ho",
            actores_principales="Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong"
        ),
        Pelicula(
            titulo="La La Land",
            descripcion="Un pianista de jazz y una actriz en busca del éxito se enamoran mientras persiguen sus sueños en Los Ángeles.",
            duracion=128,
            genero="Musical",
            director="Damien Chazelle",
            actores_principales="Ryan Gosling, Emma Stone"
        ),
    ]

    db.session.add_all(peliculas)
    db.session.commit()

    sesiones = [
        # Interstellar
        Sesion(id_pelicula=1, fecha=date(2025, 6, 10), hora=time(17, 0), sala="Sala 1"),
        Sesion(id_pelicula=1, fecha=date(2025, 6, 11), hora=time(20, 0), sala="Sala 1"),

        # El Padrino
        Sesion(id_pelicula=2, fecha=date(2025, 6, 10), hora=time(19, 0), sala="Sala 2"),
        Sesion(id_pelicula=2, fecha=date(2025, 6, 12), hora=time(21, 0), sala="Sala 3"),

        # Inception
        Sesion(id_pelicula=3, fecha=date(2025, 6, 11), hora=time(18, 30), sala="Sala 1"),
        Sesion(id_pelicula=3, fecha=date(2025, 6, 13), hora=time(22, 0), sala="Sala 2"),

        # Parasite
        Sesion(id_pelicula=4, fecha=date(2025, 6, 10), hora=time(16, 30), sala="Sala 4"),
        Sesion(id_pelicula=4, fecha=date(2025, 6, 14), hora=time(19, 30), sala="Sala 4"),

        # La La Land
        Sesion(id_pelicula=5, fecha=date(2025, 6, 15), hora=time(21, 0), sala="Sala 5"),
        Sesion(id_pelicula=5, fecha=date(2025, 6, 16), hora=time(18, 0), sala="Sala 5"),
    ]

    db.session.add_all(sesiones)
    db.session.commit()

    print("✅ Películas y sesiones insertadas correctamente.")