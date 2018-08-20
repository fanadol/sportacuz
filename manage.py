from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
import unittest

from Sportacuz import db, create_app
from SportacuzApi.models import coach

app = create_app('dev')
manager = Manager(app)
migrate = Migrate(app, db)
server = Server(threaded=True, port=5000)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)


@manager.command
def test():
    """
    Runs the unit test. 
    """
    tests = unittest.TestLoader().discover('CoachApp/api/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
