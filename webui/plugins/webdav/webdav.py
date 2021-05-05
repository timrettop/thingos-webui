import tornado.web
import subprocess


filename="/data/photoframe/conf/webdav.conf"

class WebdavHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("webdav.html", title="Webdav", webdav=readData())

    def post(self):
        data={}
        data["url"]=self.get_body_argument("url")
        data["username"]=self.get_body_argument("username")
        data["password"]=self.get_body_argument("password")
        
        writeData(data)
        
        self.render("webdav_response.html", title="Webdav")
        


def readData():
  data={}
  data["url"]=""
  data["username"]=""

  try:
    f = open(filename, "r")
  except:
    pass
  else:
    line=f.readline()
    parts=line.split()
  
    if (len(parts)==3):
      data["url"]=parts[0]
      data["username"]=parts[1]
      # Password is ignored as not needed

    f.close()
      
  return data


def writeData(data):
  f = open(filename, "w")
  f.write("{url} {username} {password}\n".format(url=data["url"], username=data["username"], password=data["password"]))
  f.close()
  
  subprocess.Popen(["photoframe.sh","sync"])

