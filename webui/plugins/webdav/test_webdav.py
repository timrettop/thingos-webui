import unittest
from unittest.mock import patch, mock_open


import webdav

class TestReadData(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data='https://your.server/with/path testuser testpassword'))
    def test_valid(self):
      webdav.readData()
      self.assertEqual(webdav.readData(), {"url":"https://your.server/with/path", "username":"testuser"})

    @patch("builtins.open", mock_open(read_data='https://your.server/with/path   testuser  testpassword'))
    def test_valid_with_spaces(self):
      webdav.readData()
      self.assertEqual(webdav.readData(), {"url":"https://your.server/with/path", "username":"testuser"})

    @patch("builtins.open", mock_open(read_data='https://your.server/with/path testuser'))
    def test_wrong_config(self):
      webdav.readData()
      self.assertEqual(webdav.readData(), {"url":"", "username":""})
      
    def test_missing_file(self):
      with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError()
        webdav.readData()
        self.assertEqual(webdav.readData(), {"url":"", "username":""})
    

#class TestWriteData(unittest.TestCase):

    #def test_valid(self):
      #data= {"url":"https://your.server/with/path", "username":"testuser", "password":"testpassword"}
      #webdav.writeData(data)



if __name__ == '__main__':
    unittest.main()


