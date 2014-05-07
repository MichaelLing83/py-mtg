import unittest
from typecheck import *
from Utilities import guarantee

class TestTypecheck(unittest.TestCase):

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
    
    def test_(self):
        '''
        Verify that Card can be initialized.
        '''
        guarantee(True, "Always true")
        self.assertRaises(InputParameterError, guarantee, ("x", "y"))
    
    
        

if __name__ == '__main__':
    unittest.main()