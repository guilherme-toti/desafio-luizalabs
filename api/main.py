# Tornado dependencies
import tornado.escape
import tornado.ioloop
# Handlers for URLS
from handlers import person, error
# Settings
from settings import Settings
from database import init_db

# Init the database
init_db()

# Routes
application = tornado.web.Application([
    (r"/person/?([0-9]+)?/?", person.Person)
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
