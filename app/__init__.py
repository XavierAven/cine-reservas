from flask import Flask, send_from_directory
from flask_cors import CORS
from .database import db
import os

def create_app():
    app = Flask(__name__, static_folder='app/static')
    app.config.from_pyfile('../config.py')

    CORS(app)  # Habilitar CORS

    db.init_app(app)

    from . import models
    from .routes import auth
    from .routes import movies

    app.register_blueprint(auth.bp)
    app.register_blueprint(movies.movies_bp)  # Usamos movies_bp

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        # Servir index.html desde la carpeta app/static
        return send_from_directory(os.path.join(app.root_path, 'app/static'), 'index.html')

    return app
