from unittest.mock import patch

from webui import server



#display.handler.isOn = display.handler.isOn_Mock
#display.handler.setOn = display.handler.setOn_Mock

#plugins.power.handler.reboot = plugins.power.handler.reboot_Mock
#plugins.power.handler.shutdown = plugins.power.handler.shutdown_Mock
@patch("webui.plugins.timezone.handler.getTimezone")
@patch("webui.plugins.timezone.handler.setTimezone")
@patch("webui.plugins.webdav.handler.writeData")
@patch("webui.plugins.webdav.handler.readData")
@patch("webui.plugins.update.handler.platformupdate.perform_update")
@patch("webui.server.update.handler.platformupdate.get_all_versions")
@patch("webui.server.update.handler.platformupdate.get_os_version")
@patch("webui.plugins.power.handler.reboot")
@patch("webui.plugins.power.handler.shutdown")
@patch("webui.plugins.display.handler.writeData")
@patch("webui.plugins.display.handler.readData")
@patch("webui.plugins.display.handler.setOn")
@patch("webui.server.display.handler.isOn")
def main_test(mock_isOn, mock_setOn, mock_readcron, mock_writecron, mock_shutdown, mock_reboot, mock_version, mock_versions, mock_update, mock_readwebdav, mock_writewebdav, mock_settimezone, mock_gettimezone):
  mock_readcron.return_value = [
    {"minute":"0", "hour":"20", "day":"*", "month":"*", "dayofweek":"*", "state":"off"},
    {"minute":"0", "hour":"8", "day":"*", "month":"*", "dayofweek":"*", "state":"on"}]
  mock_version.return_value = ("photOS", "0.0.0")
  mock_versions.return_value = ["0.0.7", "0.8.15"]
  mock_readwebdav.return_value = {"url":"https://your.server/with/path", "username":"testuser"}
  mock_gettimezone.return_value = "Europe/Berlin"
  
  server.settings["debug"]=True;
  server.port=8888;
  
  server.main()
  
if __name__ == "__main__":
    main_test()
