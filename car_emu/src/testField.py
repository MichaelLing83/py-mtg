import unittest
from Field import Field
from Utilities import PyException

class TestCard(unittest.TestCase):

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
    
    def test_init(self):
        '''
        Verify that Field can be initialized.
        '''
        self.assertTrue(Field(200, 100))
        self.assertTrue(Field(width=200, height=100))
    
    def test_lines(self):
        '''
        '''
        field = Field(200, 200)
        field.add_line(0, 0, 100, 100)
        field.add_line(100, 100, 200, 200)
        self.assertRaises(PyException, field.add_line, -1, 0, 100, 100)
        self.assertRaises(PyException, field.add_line, 0, 0, 555, 100)
        self.assertRaises(PyException, field.add_line, 0, 222, 0, 100)
        self.assertRaises(PyException, field.add_line, 0, 5, 0, 666)
        self.assertEqual(2, len(field.get_lines()))

if __name__ == '__main__':
    unittest.main()