import tornado.ioloop
import tornado.web

from .plugins import index
from .plugins import power
from .plugins import display
from .plugins import update

import os

#display.handler.isOn = display.handler.isOn_Mock
#display.handler.setOn = display.handler.setOn_Mock

#plugins.power.handler.reboot = plugins.power.handler.reboot_Mock
#plugins.power.handler.shutdown = plugins.power.handler.shutdown_Mock

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

def main():
  app= tornado.web.Application([
         (r"/", index.handler.IndexHandler),
         (r"/power", power.handler.PowerHandler),
         (r"/display", display.handler.DisplayHandler),
         (r"/update", update.handler.UpdateHandler),
         (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': settings['static_path']})
  ], **settings)

  app.listen(8888)
  tornado.ioloop.IOLoop.current().start() 
  
if __name__ == "__main__":
    main()
