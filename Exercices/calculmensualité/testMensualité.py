import unittest
from CalculMensualité import *


class testTaux(unittest.TestCase):

    def setUp(self):
        # print('setUp')
        self.credit1 = Credit(200000, 7)
        self.credit2 = Credit(200000, 10)
        self.credit3 = Credit(200000, 15)
        self.credit4 = Credit(200000, 20)

    def test_taux1(self):
        self.assertEqual(self.credit1.mensualite(),  2459.35)
        self.assertEqual(self.credit1.coute_total(),  6585.40)

    def test_taux2(self):
        self.assertEqual(self.credit2.mensualite(),  1760.78)
        self.assertEqual(self.credit2.coute_total(), 11293.60)

    def test_taux3(self):
        self.assertEqual(self.credit3.mensualite(), 1230.71)
        self.assertEqual(self.credit3.coute_total(), 21527.80)

    def test_taux4(self):
        self.assertEqual(self.credit4.mensualite(),  974.32)
        self.assertEqual(self.credit4.coute_total(),33836.80 )

    def TearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
