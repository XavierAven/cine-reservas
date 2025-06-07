from flask import Blueprint, request, jsonify
from app.models import Reserva
from app.database import db
from .auth import token_required
import datetime

reservas_bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@reservas_bp.route('', methods=['POST'])
@token_required
def crear_reserva(current_user):
    data = request.get_json()
    id_sesion = data.get('id_sesion')
    asientos = data.get('asientos')

    if not id_sesion or not asientos:
        return jsonify({'error': 'Faltan datos'}), 400

    nueva_reserva = Reserva(
        id_usuario=current_user.id,
        id_sesion=id_sesion,
        asientos=asientos,
        fecha_reserva=datetime.datetime.utcnow()
    )

    db.session.add(nueva_reserva)
    db.session.commit()

    return jsonify({'mensaje': 'Reserva creada correctamente'})

@reservas_bp.route('', methods=['GET'])
@token_required
def obtener_reservas(current_user):
    reservas = Reserva.query.filter_by(id_usuario=current_user.id).all()
    reservas_list = []
    for r in reservas:
        reservas_list.append({
            'id': r.id,
            'id_sesion': r.id_sesion,
            'asientos': r.asientos,
            'fecha_reserva': r.fecha_reserva.isoformat()
        })
    return jsonify(reservas_list)

@reservas_bp.route('/<int:reserva_id>', methods=['DELETE'])
@token_required
def eliminar_reserva(current_user, reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if not reserva or reserva.id_usuario != current_user.id:
        return jsonify({'error': 'Reserva no encontrada o no autorizada'}), 404

    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'mensaje': 'Reserva anulada correctamente'})
