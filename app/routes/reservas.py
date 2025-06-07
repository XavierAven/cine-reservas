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
