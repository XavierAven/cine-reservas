import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'supersecretkey'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'cine.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
