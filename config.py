
class Config:
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:jemila@localhost/pets'

class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options ={
  'development':DevConfig,
  'production':ProdConfig,
  'tests':TestConfig
}