# movies.py
from flask import Blueprint, jsonify
from app.models import Pelicula, Sesion

movies_bp = Blueprint('movies', __name__, url_prefix='/peliculas')

@movies_bp.route('/', methods=['GET'])
def get_peliculas():
    peliculas = Pelicula.query.all()
    return jsonify([
        {
            'id': p.id,
            'titulo': p.titulo,
            'genero': p.genero,
            'imagen_url': p.imagen_url
        }
        for p in peliculas
    ])

@movies_bp.route('/<int:pelicula_id>', methods=['GET'])
def get_pelicula_con_sesiones(pelicula_id):
    pelicula = Pelicula.query.get_or_404(pelicula_id)
    sesiones = Sesion.query.filter_by(id_pelicula=pelicula_id).all()

    return jsonify({
        'pelicula': {
            'id': pelicula.id,
            'titulo': pelicula.titulo,
            'descripcion': pelicula.descripcion,
            'duracion': pelicula.duracion,
            'genero': pelicula.genero,
            'director': pelicula.director,
            'actores_principales': pelicula.actores_principales,
            'imagen_url': pelicula.imagen_url
        },
        'sesiones': [
            {
                'fecha': sesion.fecha.isoformat(),
                'hora': sesion.hora.strftime("%H:%M"),
                'sala': sesion.sala
            }
            for sesion in sesiones
        ]
    })
