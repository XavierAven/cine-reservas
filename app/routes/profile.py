from flask import Blueprint, jsonify, request
from app.models import Usuario, Reserva, Pelicula, Sesion
from app.database import db
from .auth import token_required
import datetime

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')


@profile_bp.route('/', methods=['GET'])
@token_required
def get_profile(current_user):
    reservas = Reserva.query.filter_by(id_usuario=current_user.id).all()

    reservas_list = []
    for reserva in reservas:
        sesion = Sesion.query.get(reserva.id_sesion)
        pelicula = Pelicula.query.get(sesion.id_pelicula)
        reservas_list.append({
            'reserva_id': reserva.id,
            'pelicula_titulo': pelicula.titulo,
            'fecha': sesion.fecha.strftime('%Y-%m-%d'),
            'hora': sesion.hora.strftime('%H:%M'),
            'sala': sesion.sala,
            'asientos': reserva.asientos
        })

    return jsonify({
        'nombre': current_user.nombre,
        'email': current_user.email,
        'reservas': reservas_list
    })


@profile_bp.route('/cancelar/<int:reserva_id>', methods=['DELETE'])
@token_required
def cancelar_reserva(current_user, reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva or reserva.id_usuario != current_user.id:
        return jsonify({'error': 'Reserva no encontrada o no autorizada'}), 404

    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'mensaje': 'Reserva cancelada correctamente'})
