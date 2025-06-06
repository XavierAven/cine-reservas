from flask import Blueprint, jsonify
from app.models import Pelicula, Sesion

movies_bp = Blueprint('movies', __name__, url_prefix='/peliculas')

@movies_bp.route('/', methods=['GET'])
def get_peliculas():
    peliculas = Pelicula.query.all()
    peliculas_list = [
        {
            'id': p.id,
            'titulo': p.titulo,
            'descripcion': p.descripcion,
            'duracion': p.duracion,
            'genero': p.genero
        } for p in peliculas
    ]
    return jsonify(peliculas_list)

@movies_bp.route('/sesiones/<int:pelicula_id>', methods=['GET'])
def get_sesiones(pelicula_id):
    sesiones = Sesion.query.filter_by(id_pelicula=pelicula_id).all()
    sesiones_list = [
        {
            'id': s.id,
            'fecha': s.fecha.strftime('%Y-%m-%d'),
            'hora': s.hora.strftime('%H:%M'),
            'sala': s.sala
        } for s in sesiones
    ]
    return jsonify(sesiones_list)
