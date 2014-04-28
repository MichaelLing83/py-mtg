import unittest
from typecheck import *
from Utilities import MtgException
from MtgGame import Battlefield

class TestMtgGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_Battlefield(self):
        '''
        Verify that ...
        '''
        self.assertRaises(MtgException, Battlefield)
        self.assertRaises(MtgException, Battlefield, (1,2,3))

if __name__ == '__main__':
    unittest.main()