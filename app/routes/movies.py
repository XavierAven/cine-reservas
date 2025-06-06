from flask import Blueprint, jsonify
from ..models import Pelicula, Sesion

bp = Blueprint('movies', __name__, url_prefix='/peliculas')

@bp.route('/', methods=['GET'])
def obtener_peliculas():
    peliculas = Pelicula.query.all()
    resultado = []
    for p in peliculas:
        resultado.append({
            'id': p.id,
            'titulo': p.titulo,
            'descripcion': p.descripcion,
            'duracion': p.duracion,
            'genero': p.genero
        })
    return jsonify(resultado)

@bp.route('/sesiones/<int:pelicula_id>', methods=['GET'])
def obtener_sesiones(pelicula_id):
    sesiones = Sesion.query.filter_by(id_pelicula=pelicula_id).all()
    resultado = []
    for s in sesiones:
        resultado.append({
            'id': s.id,
            'fecha': s.fecha.strftime('%Y-%m-%d'),
            'hora': s.hora.strftime('%H:%M'),
            'sala': s.sala
        })
    return jsonify(resultado)
