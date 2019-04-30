from app import create_app
from flask_script import Server,Manager
from app.models import User

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager.add_command('server',Server)
@manager.command
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app=app)

if __name__ =='__main__':
  manager.run()