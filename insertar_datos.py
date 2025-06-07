# insertar_datos.py
import requests
from app import create_app, db
from app.models import Pelicula, Sesion
from datetime import date, time

OMDB_API_KEY = "9e446b40"

def obtener_poster(titulo):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={titulo}"
    respuesta = requests.get(url).json()
    return respuesta.get("Poster", "")

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    peliculas = [
        Pelicula("Interstellar", "Exploradores en agujero de gusano", 169, "Ciencia ficción", "Christopher Nolan", "Matthew McConaughey", obtener_poster("Interstellar")),
        Pelicula("El Padrino", "Familia mafiosa en EE.UU.", 175, "Drama", "Francis Ford Coppola", "Marlon Brando", obtener_poster("The Godfather")),
        Pelicula("Inception", "Ladrón en sueños", 148, "Thriller", "Christopher Nolan", "Leonardo DiCaprio", obtener_poster("Inception")),
        Pelicula("Parasite", "Familia pobre infiltrada en ricos", 132, "Thriller", "Bong Joon-ho", "Song Kang-ho", obtener_poster("Parasite")),
        Pelicula("La La Land", "Romance en L.A.", 128, "Musical", "Damien Chazelle", "Ryan Gosling", obtener_poster("La La Land")),
        Pelicula("Titanic", "Amor en naufragio histórico", 195, "Drama", "James Cameron", "Leonardo DiCaprio", obtener_poster("Titanic")),
        Pelicula("The Dark Knight", "Batman contra Joker", 152, "Acción", "Christopher Nolan", "Christian Bale", obtener_poster("The Dark Knight")),
        Pelicula("Avatar", "Exploración en otro planeta", 162, "Ciencia ficción", "James Cameron", "Sam Worthington", obtener_poster("Avatar")),
        Pelicula("The Matrix", "Realidad virtual peligrosa", 136, "Ciencia ficción", "Wachowski", "Keanu Reeves", obtener_poster("The Matrix")),
        Pelicula("Joker", "Origen del Joker", 122, "Drama", "Todd Phillips", "Joaquin Phoenix", obtener_poster("Joker")),
        Pelicula("Forrest Gump", "Vida extraordinaria de un hombre ordinario", 142, "Drama", "Robert Zemeckis", "Tom Hanks", obtener_poster("Forrest Gump")),
        Pelicula("Gladiator", "Venganza en la antigua Roma", 155, "Acción", "Ridley Scott", "Russell Crowe", obtener_poster("Gladiator")),
        Pelicula("The Shawshank Redemption", "Amistad en prisión", 142, "Drama", "Frank Darabont", "Tim Robbins", obtener_poster("The Shawshank Redemption")),
        Pelicula("Pulp Fiction", "Historias entrelazadas en el mundo criminal", 154, "Crimen", "Quentin Tarantino", "John Travolta", obtener_poster("Pulp Fiction")),
        Pelicula("Fight Club", "Club secreto y caos", 139, "Drama", "David Fincher", "Brad Pitt", obtener_poster("Fight Club")),
        Pelicula("Saving Private Ryan", "Búsqueda en la Segunda Guerra Mundial", 169, "Bélica", "Steven Spielberg", "Tom Hanks", obtener_poster("Saving Private Ryan")),
        Pelicula("The Lion King", "Historia del príncipe Simba", 88, "Animación", "Roger Allers", "Matthew Broderick", obtener_poster("The Lion King")),
        Pelicula("Back to the Future", "Viajes en el tiempo divertidos", 116, "Ciencia ficción", "Robert Zemeckis", "Michael J. Fox", obtener_poster("Back to the Future")),
        Pelicula("Star Wars: Episode IV - A New Hope", "Lucha galáctica épica", 121, "Ciencia ficción", "George Lucas", "Mark Hamill", obtener_poster("Star Wars")),
        Pelicula("Harry Potter and the Sorcerer's Stone", "Inicio del joven mago", 152, "Fantasía", "Chris Columbus", "Daniel Radcliffe", obtener_poster("Harry Potter and the Sorcerer's Stone"))
    ]

    db.session.add_all(peliculas)
    db.session.commit()

    print("✅ Películas insertadas con imágenes correctamente.")
