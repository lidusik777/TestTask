import unittest
PATH = "data_price_CELYAD"

class Test_init(unittest.TestCase):
    def setUp(self):
        try:
            f = open(PATH, 'rU')
        except Exception as Ex:
            print("You need file to test this script", Ex)
