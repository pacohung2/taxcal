import taxcal
import unittest

class TestTaxCal(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(taxcal.tax('seperate',500000)[1], 41500)
        self.assertEqual(taxcal.tax('seperate',750000)[1], 84000)
        self.assertEqual(taxcal.tax('joint',500000+750000)[1], 143500)
        self.assertEqual(taxcal.tax('seperate',1)[1], 0)
        self.assertEqual(taxcal.tax('seperate',999999999)[1], 149997299)
        self.assertEqual(taxcal.tax('seperate',600000)[1], 58500)
        self.assertEqual(taxcal.tax('seperate',550000)[1], 50000)
        self.assertEqual(taxcal.tax('joint',600000+550000)[1], 126500)
        self.assertEqual(taxcal.tax('joint',900000+400000)[1], 152000)
        self.assertEqual(taxcal.tax('seperate',666666)[1], 69833)
        self.assertEqual(taxcal.tax('seperate',777777)[1], 88722)
        self.assertEqual(taxcal.tax('joint',666666+777777)[1], 176555)
        self.assertEqual(taxcal.tax('seperate',360000)[1], 17700)
        self.assertEqual(taxcal.tax('joint',360000+360000)[1], 53400)
        self.assertEqual(taxcal.tax('seperate',8000000)[1], 1197300)
        self.assertEqual(taxcal.tax('joint',8000000+360000)[1], 1248600)
        self.assertEqual(taxcal.tax('seperate',33333333)[1], 4997299)

if __name__ == '__main__':
    unittest.main()
