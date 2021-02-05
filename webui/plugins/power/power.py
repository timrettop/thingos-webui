import tornado.web

import subprocess

class PowerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("power.html", title="Power")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        if (self.get_body_argument("action")=="shutdown"):
            shutdown()
        if (self.get_body_argument("action")=="reboot"):
            reboot();
        self.write("You wrote " + self.get_body_argument("action"))


def shutdown():
  subprocess.check_output(["shutdown"])
  
def shutdown_Mock():
  pass

def reboot():
  subprocess.check_output(["reboot"])
  
def reboot_Mock():
  pass

