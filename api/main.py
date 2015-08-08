# Tornado dependencies
import tornado.escape
import tornado.ioloop
# Handlers for URLS
from handlers import person
# Settings
from settings import Settings

# Routes
application = tornado.web.Application([
    (r"/", person.Person)
])
 
if __name__ == "__main__":
    application.listen(Settings().getApiPort())
    tornado.ioloop.IOLoop.instance().start()
