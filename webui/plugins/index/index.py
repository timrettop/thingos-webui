import tornado.web
import tornado.ioloop
import base64
import functools
import hashlib,base64,random

API_KEYS = {
	'rjtzWc674hDxTSWulgETRqHrVVQoI3T8f9RoMlO6zsQ': 'test'
}


def api_auth(username, password):
	if username in API_KEYS:
		return True
	return False
	

def basic_auth(auth):
	def decore(f):
		def _request_auth(handler):
			handler.set_header('WWW-Authenticate', 'Basic realm=JSL')
			handler.set_status(401)
			handler.finish()
			return False
		
		@functools.wraps(f)
		def new_f(*args):
			handler = args[0]
 
			auth_header = handler.request.headers.get('Authorization')
			if auth_header is None: 
				return _request_auth(handler)
			if not auth_header.lower().startswith('Basic '): 
				return _request_auth(handler)
 
			auth_decoded = base64.b64decode(auth_header[6:]).decode('ascii')
			username, password = auth_decoded.split(':', 1)
 
			if (auth(username, password)):
				f(*args)
			else:
				_request_auth(handler)
					
		return new_f
	return decore


class IndexHandler(tornado.web.RequestHandler):
    @basic_auth(api_auth)
    def get(self):
        self.render("index.html", title="photOS")
