import datetime
import logging

from tornado import ioloop
import tornado.web

from . import platformupdate


class UpdateHandler(tornado.web.RequestHandler):
    def get(self):
        versions=platformupdate.get_all_versions()
        current_version=platformupdate.get_os_version()
        self.render("update.html", title="Update", version=current_version, versions=versions)

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Updating to " + self.get_body_argument("version"))
        
        #Wait to finish request
        ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=2),
                                             platformupdate.perform_update, version=self.get_body_argument("version"))
