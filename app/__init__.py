from flask import Flask, send_from_directory
from flask_cors import CORS
from .database import db
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile('../config.py')

    CORS(app)  # Habilitar CORS

    db.init_app(app)

    from . import models
    from .routes import auth
    from .routes import movies  # ✅ AÑADIDO

    app.register_blueprint(auth.bp)
    app.register_blueprint(movies.bp)  # ✅ CORREGIDO

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        # Sirve el index.html desde la carpeta static
        return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

    return app
