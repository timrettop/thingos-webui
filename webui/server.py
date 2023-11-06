import tornado.ioloop
import tornado.web
import tornado_http_auth

from .plugins import index
from .plugins import power
from .plugins import display
from .plugins import update
from .plugins import webdav
from .plugins import timezone

import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

port=80

def main():
  app= tornado.web.Application([
         (r"/", index.handler.IndexHandler),
         (r"/power", power.handler.PowerHandler),
         (r"/display", display.handler.DisplayHandler),
         (r"/update", update.handler.UpdateHandler),
         (r"/webdav", webdav.handler.WebdavHandler),
         (r"/timezone", timezone.handler.TimezoneHandler),
         (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': settings['static_path']})
  ], **settings)

  app.listen(port)
  tornado.ioloop.IOLoop.current().start() 
  
if __name__ == "__main__":
    main()
