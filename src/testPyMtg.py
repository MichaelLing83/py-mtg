import unittest
from pyMtg import pyMtg
import Constants

class TestPyMtg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
    
    def setUp(self):
        self.pymtg = pyMtg()
    
    def tearDown(self):
        pass
    
    def test_version(self):
        '''
        Verify version command.
        '''
        self.pymtg.onecmd("version")
        self.assertEqual(self.pymtg.last_cli_output, Constants.VERSION)
    
    
        

if __name__ == '__main__':
    unittest.main()