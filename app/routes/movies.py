from flask import Blueprint, jsonify
from app.models import Pelicula, Sesion

movies_bp = Blueprint('movies', __name__, url_prefix='/peliculas')

@movies_bp.route('/', methods=['GET'])
def get_peliculas():
    peliculas = Pelicula.query.all()
    peliculas_list = [p.to_dict() for p in peliculas]
    return jsonify(peliculas_list)

@movies_bp.route('/<int:pelicula_id>', methods=['GET'])
def get_pelicula_con_sesiones(pelicula_id):
    pelicula = Pelicula.query.get(pelicula_id)
    if not pelicula:
        return jsonify({'error': 'Película no encontrada'}), 404

    sesiones = Sesion.query.filter_by(id_pelicula=pelicula_id).all()
    return jsonify({
        'pelicula': pelicula.to_dict(),
        'sesiones': [s.to_dict() for s in sesiones]
    })