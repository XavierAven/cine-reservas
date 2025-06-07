from flask import Blueprint, request, jsonify
from app.models import Reserva, Asiento
from app.database import db
from .auth import token_required
import datetime

reservas_bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@reservas_bp.route('', methods=['POST'])
@token_required
def crear_reserva(current_user):
    data = request.get_json()
    id_sesion = data.get('id_sesion')
    num_entradas = data.get('num_entradas')

    if not id_sesion or not num_entradas:
        return jsonify({'error': 'Faltan datos'}), 400

    try:
        num_entradas = int(num_entradas)
        if num_entradas <= 0:
            return jsonify({'error': 'Número de entradas inválido'}), 400
    except:
        return jsonify({'error': 'Número de entradas debe ser un entero'}), 400

    # Obtener asientos disponibles para esa sesión
    asientos_disponibles = Asiento.query.filter_by(id_sesion=id_sesion, reservado=False).limit(num_entradas).all()

    if len(asientos_disponibles) < num_entradas:
        return jsonify({'error': 'No hay suficientes asientos disponibles'}), 400

    # Reservar los asientos
    for asiento in asientos_disponibles:
        asiento.reservado = True
        db.session.add(asiento)

    reserva = Reserva(
        id_usuario=current_user.id,
        id_sesion=id_sesion,
        asientos=','.join([str(a.numero_asiento) for a in asientos_disponibles]),
        fecha_reserva=datetime.datetime.utcnow()
    )
    db.session.add(reserva)
    db.session.commit()

    return jsonify({'mensaje': 'Reserva creada correctamente'})

@reservas_bp.route('/usuario', methods=['GET'])
@token_required
def obtener_reservas_usuario(current_user):
    reservas = Reserva.query.filter_by(id_usuario=current_user.id).all()
    resultado = []
    for r in reservas:
        resultado.append({
            'id': r.id,
            'id_sesion': r.id_sesion,
            'asientos': r.asientos,
            'fecha_reserva': r.fecha_reserva.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(resultado)

@reservas_bp.route('/<int:id_reserva>', methods=['DELETE'])
@token_required
def anular_reserva(current_user, id_reserva):
    reserva = Reserva.query.get(id_reserva)
    if not reserva or reserva.id_usuario != current_user.id:
        return jsonify({'error': 'Reserva no encontrada o no autorizada'}), 404

    # Liberar los asientos reservados
    asientos = reserva.asientos.split(',')
    for asiento_num in asientos:
        asiento = Asiento.query.filter_by(id_sesion=reserva.id_sesion, numero_asiento=asiento_num).first()
        if asiento:
            asiento.reservado = False

    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'mensaje': 'Reserva anulada correctamente'})
