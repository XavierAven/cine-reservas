from flask import Blueprint, request, jsonify
from app.models import Pago, Reserva
from app.database import db
from .auth import token_required

pagos_bp = Blueprint('pagos', __name__, url_prefix='/pagos')

@pagos_bp.route('/simular', methods=['POST'])
@token_required
def simular_pago(current_user):
    data = request.get_json()
    id_reserva = data.get('id_reserva')
    numero_tarjeta = data.get('numero_tarjeta')
    fecha_caducidad = data.get('fecha_caducidad')
    ccv = data.get('ccv')

    if not id_reserva or not numero_tarjeta or not fecha_caducidad or not ccv:
        return jsonify({'error': 'Faltan datos para el pago'}), 400

    reserva = Reserva.query.get(id_reserva)
    if not reserva or reserva.id_usuario != current_user.id:
        return jsonify({'error': 'Reserva no encontrada o no autorizada'}), 404

    # Simulación: simplemente aceptamos cualquier dato y devolvemos éxito
    nuevo_pago = Pago(
        id_reserva=id_reserva,
        metodo='Tarjeta',
        estado='Pagado'
    )
    db.session.add(nuevo_pago)
    db.session.commit()

    return jsonify({'mensaje': 'Pago simulado exitosamente', 'estado': 'Pagado'})
