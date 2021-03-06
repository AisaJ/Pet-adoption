import os
class Config:
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:jemila@localhost/pets'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY=os.environ.get('SECRET_KEY')
  # simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  # configure UploadSet
  #configure_uploads(app,photos)
  UPLOADED_PHOTOS_DEST ='app/static/photos'


#  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  SUBJECT_PREFIX = 'Pet-adoption'
  SENDER_EMAIL = 'aisajam.jammy@gmail.com'


class ProdConfig(Config):
  # pass
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options ={
  'development':DevConfig,
  'production':ProdConfig,
  'tests':TestConfig
}