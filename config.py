
class Config:
  pass

  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # configure UploadSet
  configure_uploads(app,photos)

# simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

#  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options ={
  'development'= DevConfig,
  'production'= ProdConfig,
  'tests'= TestConfig
}