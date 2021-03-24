import taxcalbest
import unittest

class TestTaxCal(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(taxcalbest.tax('seperate',500000)[0], 41500)
        self.assertEqual(taxcalbest.tax('seperate',750000)[0], 84000)
        self.assertEqual(taxcalbest.tax('joint',500000+750000)[0], 143500)
        self.assertEqual(taxcalbest.tax('seperate',1)[0], 0)
        self.assertEqual(taxcalbest.tax('seperate',999999999)[0], 149997299)
        self.assertEqual(taxcalbest.tax('joint',0+750000)[0], 61560)

if __name__ == '__main__':
    unittest.main()