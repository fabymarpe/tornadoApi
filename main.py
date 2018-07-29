import os
import json
import tornado.httpserver
import tornado.ioloop
from tornado.web import Application, url, RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello world")

    def set_default_headers(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")


class Login(MainHandler):

    def post(self):
        data = json.loads(self.request.body)
        if data['email'] == 'no-email@no-email.com' and data['password'] == \
                '12345':
            user = {
                'name': 'testUser',
                'email': data['email'],
                'address': 'addressUser'
            }
            response = {
                'code': 200,
                'msg': user
            }
        else:
            response = {'code': 401,
                        'msg': 'email y/o password incorrect.'}
        self.write(response)


class Logout(MainHandler):

    def post(self):
        data = json.loads(self.request.body)
        if data['email'] == 'no-email@no-email.com':
            response = {
                'code': 200,
                'msg': 'Goodbay'
            }
        else:
            response = {'code': 401,
                        'msg': "User isn't login"}
        self.write(response)


class Loan(MainHandler):

    def post(self):
        data = json.loads(self.request.body)
        requested_amount = int(data['business'].get('requestedAmount', 0))
        if requested_amount > 50000:
            message = 'Declined'
        elif requested_amount == 50000:
            message = 'Undecided'
        else:
            message = 'Approved'
        response = {'code': 200,
                    'msg': message}
        self.write(response)


def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r"/login", Login),
        url(r"/logout", Logout),
        url(r"/loan", Loan, name='loan')
    ])


def main():
    http_server = tornado.httpserver.HTTPServer(make_app())
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()