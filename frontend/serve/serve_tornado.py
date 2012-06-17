import sys
from os.path import normpath, join, abspath, dirname
sys.path.append(normpath(join(abspath(dirname(__file__)), '../../')))

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application

from frontend import app

flask_cont = WSGIContainer(app)

application = Application([
(r".*", FallbackHandler, dict(fallback=flask_cont)),
])

if __name__ == "__main__":
    application.listen(80)
    IOLoop.instance().start()
