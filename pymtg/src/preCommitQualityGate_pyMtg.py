import unittest
from os import getcwd

if __name__ == '__main__':
    suites = unittest.TestLoader().discover(start_dir=getcwd())
    unittest.runner.TextTestRunner().run(suites)
