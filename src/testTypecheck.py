import unittest
from typecheck import *
from Utilities import garantee

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
        garantee(True, "Always true")
        self.assertRaises(InputParameterError, garantee, ("x", "y"))
    
    
        

if __name__ == '__main__':
    unittest.main()