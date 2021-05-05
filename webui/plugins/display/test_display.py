import unittest
from unittest.mock import patch, mock_open


import display

class TestReadData(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data='0   20 * * * /usr/bin/photoframe.sh display off'))
    def test_valid(self):
      self.assertDictEqual(display.readData()[0], {"minute":"0", "hour":"20", "day":"*", "month":"*",                                      "dayofweek":"*", "state":"off"})
    

class TestWriteData(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data='0   19 * * * /usr/bin/photoframe.sh display off\n*/15 * * * * /usr/sbin/dyndns-update'))
    def test_valid(self):
      rules=[{"minute":"0", "hour":"20", "day":"*", "month":"*", "dayofweek":"*", "state":"off"}]
      display.writeData(rules)
      
class TestWriteDelay(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data='SLIDESHOW_DELAY=112\nANOTHER_ITEM=Hello'))
    def test_valid(self):
      display.setDelay(10)


if __name__ == '__main__':
    unittest.main()


