from flask import Blueprint, jsonify
from app.models import Pelicula, Sesion
from app.database import db

movies_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET'])
def listar_peliculas():
    peliculas = Pelicula.query.all()
    resultado = []
    for peli in peliculas:
        sesiones = Sesion.query.filter_by(id_pelicula=peli.id).all()
        sesiones_info = [{
            "fecha": s.fecha.isoformat(),
            "hora": s.hora.strftime("%H:%M"),
            "sala": s.sala
        } for s in sesiones]

        resultado.append({
            "id": peli.id,
            "titulo": peli.titulo,
            "descripcion": peli.descripcion,
            "duracion": peli.duracion,
            "genero": peli.genero,
            "sesiones": sesiones_info
        })

    return jsonify(resultado)
