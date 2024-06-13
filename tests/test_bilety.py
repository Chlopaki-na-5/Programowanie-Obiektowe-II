import unittest
from src.bilet import BiletFactory, Bilet, BiletNormalny, BiletUlgowy

class TestBilet(unittest.TestCase):
    def test_bilet_creation(self):
        bilet = BiletFactory.create_bilet('normalny')
        self.assertIsInstance(bilet, BiletNormalny)

        bilet = BiletFactory.create_bilet('ulgowy')
        self.assertIsInstance(bilet, BiletUlgowy)

        bilet = BiletFactory.create_bilet('inny')
        self.assertIsInstance(bilet, Bilet)

    def test_bilet_normalny_price(self):
        bilet = BiletFactory.create_bilet('normalny')
        bilet.change_count(2)
        self.assertEqual(bilet.price(), '8.00 zł')

    def test_bilet_ulgowy_price(self):
        bilet = BiletFactory.create_bilet('ulgowy')
        bilet.change_count(3)
        self.assertEqual(bilet.price(), '6.00 zł')

if __name__ == '__main__':
    unittest.main()
