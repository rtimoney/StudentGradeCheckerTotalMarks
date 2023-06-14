import unittest
from functions import getTotal

class TestGetTotal(unittest.TestCase):
    def test_(self):
        self.assertEqual(getTotal('software engineering,100newlinedatabases,25newlineweb development,25newlinecomputing foundations,25newlinecloud computing,100'),275)

    def test_2(self):
        self.assertEqual(getTotal('software engineering,100newlinedatabases,50newlineweb development,25newlinecomputing foundations,25newlinecloud computing,100'),300)

    def test_3(self):
        self.assertEqual(getTotal('software engineering,50newlinedatabases,25newlineweb development,25newlinecomputing foundations,25newlinecloud computing,100'),225)

    def test_4(self):
        self.assertEqual(getTotal('software engineering,0newlinedatabases,0newlineweb development,0newlinecomputing foundations,0newlinecloud computing,0'),0)




if __name__ == '__main__':
    unittest.main()
