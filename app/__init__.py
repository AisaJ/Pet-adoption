from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manger = LoginManager()
login_manger.session_protection = 'strong'
login_manger.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)

  #Blueprint registrations
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initializing flask extenstions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manger.init_app(app)

  return app