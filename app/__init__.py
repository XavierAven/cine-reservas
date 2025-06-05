from flask import Flask
from flask_cors import CORS
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    CORS(app)  # Habilitar CORS

    db.init_app(app)

    from . import models
    from .routes import auth
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return '¡Servidor Flask funcionando!'

    return app
