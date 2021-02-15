import tornado.web

import os
import re
import glob

timezones_folder="/usr/share/zoneinfo"
localtime_link="/data/etc/localtime"


class TimezoneHandler(tornado.web.RequestHandler):
    def get(self):
        timezone=getTimezone()
        timezones=getAllTimezones()
        self.render("timezone.html", title="Timezone", timezone=timezone, timezones=timezones)

    def post(self):
        setTimezone(self.get_body_argument("timezone"))
        self.redirect("/timezone")


def getTimezoneFromPath(path):
  tz="not set"
  match=re.search(timezones_folder + '/(.+)', path)
  if (match):
    tz=match.group(1)
    
  return tz

def getTimezone():
  tz=getTimezoneFromPath(os.readlink(localtime_link))
  return tz
  
def getAllTimezones():
  paths=glob.glob(timezones_folder+'/*/*')
  timezones=[]
  for path in paths:
    timezone=getTimezoneFromPath(path)
    if re.match('(Etc|posix|right)', timezone)==None:
      timezones.append(timezone)
  
  timezones.sort()
  
  return timezones


def setTimezone(tz):
  target=timezones_folder+"/"+tz
  
  os.symlink(target, localtime_link+"_tmp")
  os.rename(localtime_link+"_tmp", localtime_link)
