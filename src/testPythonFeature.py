import unittest
from typecheck import *
import types

class TestPythonFeature(unittest.TestCase):

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
    
    def test_method_redefine(self):
        '''
        Verify that object methods can be redefined on-the-fly.
        '''
        class A:
            def __init__(self):
                pass
            def say_hi(self):
                return "hi"
        
        a = A()
        self.assertEqual(a.say_hi(), "hi")
        def say_hi(self):
            return "hej"
        a.__setattr__(say_hi.__name__, types.MethodType(say_hi, a))
        self.assertEqual(a.say_hi(), "hej")

if __name__ == '__main__':
    unittest.main()