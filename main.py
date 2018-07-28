import os
import tornado.httpserver
import tornado.ioloop
from tornado.web import Application, url, RequestHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")


def make_app():
    return Application([
        url(r"/", MainHandler)
    ])


def main():
    http_server = tornado.httpserver.HTTPServer(make_app())
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()