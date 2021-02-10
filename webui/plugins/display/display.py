import tornado.web

import subprocess
import re

class DisplayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("display.html", title="Display", isOn=isOn())

    def post(self):
        self.set_header("Content-Type", "text/plain")
        if (self.get_body_argument("action")=="off"):
            setOn(False)
        else:              
            setOn(True)

        self.redirect("/display")


def isOn():
    result=subprocess.check_output(["vcgencmd", "display_power"], encoding="utf-8")
    match=re.search('display_power=(.)', result)
    return (match.group(1)== "1")

def isOn_Mock():
    return True



def setOn(state):
    if (state):
      subprocess.check_output(["vcgencmd", "display_power", "1"])
    else: 
      subprocess.check_output(["vcgencmd", "display_power", "0"])

def setOn_Mock(state):
    pass
