import tornado.web

class Person(tornado.web.RequestHandler):
    def get(self):
        response = { 'Hello': 'World!' }
        self.write(response)