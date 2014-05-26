import unittest
from MtgMath import MtgMath

class TestMtgMath(unittest.TestCase):

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
    
    def test_n_factorial(self):
        '''
        Verify n! calculation is correct.
        '''
        self.assertEqual(MtgMath.n_factorial(0), 1)
        self.assertEqual(MtgMath.n_factorial(10), 3628800)
    
    def test_C(self):
        '''
        Verify C(n, r) calculation.
        '''
        self.assertEqual(MtgMath.C(1, 1), 1)
        self.assertEqual(MtgMath.C(0, 0), 1)
        self.assertEqual(MtgMath.C(10, 2), 45)

if __name__ == '__main__':
    unittest.main()