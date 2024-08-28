import tornado.ioloop
import tornado.web

class UsersHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("POST => users => create")

    def get(self):
        self.write("GET => users => list")

    def patch(self):
        self.write("PATCH => users => update")

    def put(self):
        self.write("PUT => users => replace")

    def delete(self):
        self.write("DELETE => users => destroy")


def make_app():
    return tornado.web.Application([
        (r"/users", UsersHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(4000)
    print("El servidor se está ejecutando en http://localhost:4000")
    tornado.ioloop.IOLoop.current().start()
