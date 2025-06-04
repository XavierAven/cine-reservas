from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.database import db
from app.models import Usuario

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')

    if not nombre or not email or not password:
        return jsonify({'error': 'Faltan datos'}), 400

    if Usuario.query.filter_by(email=email).first():
        return jsonify({'error': 'El email ya está registrado'}), 400

    nuevo_usuario = Usuario(
        nombre=nombre,
        email=email,
        password=generate_password_hash(password)
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario registrado correctamente'})
