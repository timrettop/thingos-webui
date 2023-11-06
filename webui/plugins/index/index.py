import tornado.web
import tornado_http_auth
import base64
import functools
import hashlib,base64,random

credentials = {
	'test': 'changeme'
}

class IndexHandler(tornado_http_auth.BasicAuthMixin, tornado.web.RequestHandler):
    def prepare(self):
        self.get_authenticated_user(check_credentials_func=credentials.get, realm='Protected')
    def get(self):
        self.render("index.html", title="photOS")
