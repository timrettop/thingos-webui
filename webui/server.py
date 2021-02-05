import tornado.ioloop
import tornado.web

from .plugins import index
from .plugins import power
from .plugins import display
from .plugins import update


#plugins.display.handler.isOn = plugins.display.handler.isOn_Mock
#plugins.display.handler.setOn = plugins.display.handler.setOn_Mock

#plugins.power.handler.reboot = plugins.power.handler.reboot_Mock
#plugins.power.handler.shutdown = plugins.power.handler.shutdown_Mock

def main():
  app= tornado.web.Application([
         (r"/", index.handler.IndexHandler),
         (r"/power", power.handler.PowerHandler),
         (r"/display", display.handler.DisplayHandler),
         (r"/update", update.handler.UpdateHandler),
  ])

  app.listen(8888)
  tornado.ioloop.IOLoop.current().start() 
  
if __name__ == "__main__":
    main()
