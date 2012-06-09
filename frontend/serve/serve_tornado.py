from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
import sys
sys.path.append('../../')
from frontend import app

flask_cont = WSGIContainer(app)

application = Application([
(r".*", FallbackHandler, dict(fallback=flask_cont)),
])

if __name__ == "__main__":
    application.listen(5000)
    IOLoop.instance().start()
