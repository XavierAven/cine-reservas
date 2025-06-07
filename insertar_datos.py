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
        Pelicula(
            titulo="Titanic",
            descripcion="Historia épica de amor en el famoso naufragio.",
            duracion=195,
            genero="Drama",
            director="James Cameron",
            actores_principales="Leonardo DiCaprio, Kate Winslet"
        ),
        Pelicula(
            titulo="The Dark Knight",
            descripcion="Batman lucha contra el Joker para salvar Gotham City.",
            duracion=152,
            genero="Acción",
            director="Christopher Nolan",
            actores_principales="Christian Bale, Heath Ledger"
        ),
        Pelicula(
            titulo="Avatar",
            descripcion="Exploración de un planeta alienígena y conflicto cultural.",
            duracion=162,
            genero="Ciencia ficción",
            director="James Cameron",
            actores_principales="Sam Worthington, Zoe Saldana"
        ),
        Pelicula(
            titulo="The Matrix",
            descripcion="Realidad virtual y lucha contra el control de máquinas.",
            duracion=136,
            genero="Ciencia ficción",
            director="Hermanas Wachowski",
            actores_principales="Keanu Reeves, Laurence Fishburne"
        ),
        Pelicula(
            titulo="Joker",
            descripcion="Origen del famoso villano de Gotham City.",
            duracion=122,
            genero="Drama",
            director="Todd Phillips",
            actores_principales="Joaquin Phoenix"
        ),
        Pelicula(
            titulo="Forrest Gump",
            descripcion="La vida extraordinaria de un hombre ordinario.",
            duracion=142,
            genero="Drama",
            director="Robert Zemeckis",
            actores_principales="Tom Hanks"
        ),
        Pelicula(
            titulo="Gladiator",
            descripcion="Venganza en la antigua Roma.",
            duracion=155,
            genero="Acción",
            director="Ridley Scott",
            actores_principales="Russell Crowe"
        ),
        Pelicula(
            titulo="The Shawshank Redemption",
            descripcion="Amistad y esperanza dentro de una prisión.",
            duracion=142,
            genero="Drama",
            director="Frank Darabont",
            actores_principales="Tim Robbins, Morgan Freeman"
        ),
        Pelicula(
            titulo="Pulp Fiction",
            descripcion="Historias entrelazadas en el mundo criminal.",
            duracion=154,
            genero="Crimen",
            director="Quentin Tarantino",
            actores_principales="John Travolta, Samuel L. Jackson"
        ),
        Pelicula(
            titulo="Fight Club",
            descripcion="Un club secreto que provoca caos y auto descubrimiento.",
            duracion=139,
            genero="Drama",
            director="David Fincher",
            actores_principales="Brad Pitt, Edward Norton"
        ),
        Pelicula(
            titulo="Saving Private Ryan",
            descripcion="Búsqueda en la Segunda Guerra Mundial.",
            duracion=169,
            genero="Bélica",
            director="Steven Spielberg",
            actores_principales="Tom Hanks"
        ),
        Pelicula(
            titulo="The Lion King",
            descripcion="Historia del príncipe Simba en la sabana africana.",
            duracion=88,
            genero="Animación",
            director="Roger Allers",
            actores_principales="Matthew Broderick"
        ),
        Pelicula(
            titulo="Back to the Future",
            descripcion="Viajes en el tiempo divertidos y peligrosos.",
            duracion=116,
            genero="Ciencia ficción",
            director="Robert Zemeckis",
            actores_principales="Michael J. Fox"
        ),
        Pelicula(
            titulo="Star Wars: Episode IV - A New Hope",
            descripcion="Lucha épica en una galaxia muy, muy lejana.",
            duracion=121,
            genero="Ciencia ficción",
            director="George Lucas",
            actores_principales="Mark Hamill, Harrison Ford"
        ),
        Pelicula(
            titulo="Harry Potter and the Sorcerer's Stone",
            descripcion="Inicio de la aventura del joven mago Harry Potter.",
            duracion=152,
            genero="Fantasía",
            director="Chris Columbus",
            actores_principales="Daniel Radcliffe, Emma Watson"
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

        # Sesiones extra para nuevas películas (ajusta a gusto)
        Sesion(id_pelicula=6, fecha=date(2025, 6, 20), hora=time(19, 0), sala="Sala 1"),
        Sesion(id_pelicula=7, fecha=date(2025, 6, 21), hora=time(18, 0), sala="Sala 2"),
        Sesion(id_pelicula=8, fecha=date(2025, 6, 22), hora=time(20, 0), sala="Sala 3"),
        Sesion(id_pelicula=9, fecha=date(2025, 6, 23), hora=time(17, 30), sala="Sala 4"),
        Sesion(id_pelicula=10, fecha=date(2025, 6, 24), hora=time(21, 0), sala="Sala 5"),
        Sesion(id_pelicula=11, fecha=date(2025, 6, 25), hora=time(19, 30), sala="Sala 1"),
        Sesion(id_pelicula=12, fecha=date(2025, 6, 26), hora=time(20, 0), sala="Sala 2"),
        Sesion(id_pelicula=13, fecha=date(2025, 6, 27), hora=time(18, 30), sala="Sala 3"),
        Sesion(id_pelicula=14, fecha=date(2025, 6, 28), hora=time(17, 0), sala="Sala 4"),
        Sesion(id_pelicula=15, fecha=date(2025, 6, 29), hora=time(21, 0), sala="Sala 5"),
        Sesion(id_pelicula=16, fecha=date(2025, 6, 30), hora=time(19, 0), sala="Sala 1"),
        Sesion(id_pelicula=17, fecha=date(2025, 7, 1), hora=time(18, 0), sala="Sala 2"),
        Sesion(id_pelicula=18, fecha=date(2025, 7, 2), hora=time(20, 0), sala="Sala 3"),
        Sesion(id_pelicula=19, fecha=date(2025, 7, 3), hora=time(21, 30), sala="Sala 4"),
        Sesion(id_pelicula=20, fecha=date(2025, 7, 4), hora=time(17, 30), sala="Sala 5"),
    ]

    db.session.add_all(sesiones)
    db.session.commit()

    print("✅ Películas y sesiones insertadas correctamente.")
