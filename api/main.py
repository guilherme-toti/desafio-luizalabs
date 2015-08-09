# Logging dependences
import sys
import logging

# Tornado dependencies
import tornado.escape
import tornado.ioloop
import tornado.options

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

# Config for logging
args = sys.argv
args.append("--log_file_prefix=logs/application.log")
tornado.options.parse_command_line(args)

if __name__ == "__main__":
	# Log that API has started
	logging.info('Starting API')
	# Listen to port 8888
	application.listen(8888)
	# Start API
	tornado.ioloop.IOLoop.instance().start()
