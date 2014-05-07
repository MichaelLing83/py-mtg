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
    
    def test_deck_load(self):
        '''
        Verify deck_load command.
        '''
        self.pymtg.onecmd("deck_load BW_Token_Modem.deck")
        self.assertNotIn("Unknown syntax", self.pymtg.last_cli_output)
        self.assertNotIn("Loading failed for deck", self.pymtg.last_cli_output)

if __name__ == '__main__':
    unittest.main()