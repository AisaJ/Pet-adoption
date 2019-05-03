from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

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

  return app