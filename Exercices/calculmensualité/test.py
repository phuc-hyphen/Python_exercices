# -*- coding: utf-8 -*-
# Illustration du fonctionnement de unitest et difference entre setUp et setUpClass, tearDown et tearDownClass
import unittest
from CalculMensualité import *

class testTaux(unittest.TestCase):
    def setUp(self):
            # print('setUp')
        self.credit1 = Credit(10000, 7)
        self.credit2 = Credit(10000, 10)
        self.credit3 = Credit(10000, 15)
        self.credit4 = Credit(10000, 20)

    def test_taux1(self):
        self.assertEqual(self.credit1.taux(), 0.92)

    def test_taux2(self):
        self.assertEqual(self.credit2.taux(), 1.1)

    def test_taux3(self):
        self.assertEqual(self.credit3.taux(), 1.38)

    def test_taux4(self):
        self.assertEqual(self.credit4.taux(), 1.6)

    def tearDown(self):
        # print ('tearDown')
        pass

if __name__ == "__main__":
    unittest.main()
