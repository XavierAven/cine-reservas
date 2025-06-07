from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from .database import db
import os
from app.models import Asiento

def create_app():
    app = Flask(__name__, static_folder='app/static')
    app.config.from_pyfile('../config.py')

    CORS(app)

    db.init_app(app)

    from . import models
    from .routes import auth
    from .routes import movies
    from .routes import reservas
    from .routes import pagos

    app.register_blueprint(auth.bp)
    app.register_blueprint(movies.movies_bp)
    app.register_blueprint(reservas.reservas_bp)
    app.register_blueprint(pagos.pagos_bp)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

    @app.route('/index.html')
    def index_html():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

    @app.route('/pelicula.html')
    def pelicula():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'pelicula.html')

    @app.route('/perfil.html')
    def perfil():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'perfil.html')

    @app.route('/asientos/<int:id_sesion>', methods=['GET'])
    def obtener_asientos(id_sesion):
        asientos = Asiento.query.filter_by(id_sesion=id_sesion).all()
        if len(asientos) < 50:
            existentes = {a.numero_asiento for a in asientos}
            for i in range(1, 51):
                if i not in existentes:
                    nuevo_asiento = Asiento(id_sesion=id_sesion, numero_asiento=i, reservado=False)
                    db.session.add(nuevo_asiento)
            db.session.commit()
            asientos = Asiento.query.filter_by(id_sesion=id_sesion).all()

        return jsonify({
            "asientos": [a.to_dict() for a in asientos]
        })

    return app
