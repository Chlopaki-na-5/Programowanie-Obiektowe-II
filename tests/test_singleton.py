import unittest
from src.singleton_meta import SingletonMeta


class TestSingletonMeta(unittest.TestCase):
    def test_singleton_instance(self):
        class SingletonClass(metaclass=SingletonMeta):
            pass

        instance1 = SingletonClass()
        instance2 = SingletonClass()

        self.assertIs(instance1, instance2)


import unittest
import tkinter as tk
from unittest.mock import MagicMock
from src.gui_pages import StartPage, Bilet_page, Ilosc_Biletow_page, Pay_page, End_page, State

class TestStartPage(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = StartPage(self.root, MagicMock())

    def test_initialization(self):
        self.assertIsNotNone(self.app.controller)
        self.assertIsInstance(self.app.controller, MagicMock)
        # Add more assertions as needed for initialization

    def test_timer(self):
        self.app.timer()  # Test timer functionality

    def test_change_page(self):
        self.app.change_page()  # Test change page functionality

    def tearDown(self):
        self.root.destroy()



class TestIloscBiletowPage(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = Ilosc_Biletow_page(self.root, MagicMock())

    def test_initialization(self):
        self.assertIsNotNone(self.app.controller)
        self.assertIsInstance(self.app.controller, MagicMock)
        # Add more assertions as needed for initialization

    def test_change_count(self):
        self.app.change_count(1)  # Test change count functionality

    def test_change_page(self):
        self.app.change_page(1)  # Test change page functionality

    def tearDown(self):
        self.root.destroy()


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



class TestEndPage(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = End_page(self.root, MagicMock())

    def test_initialization(self):
        self.assertIsNotNone(self.app.controller)
        self.assertIsInstance(self.app.controller, MagicMock)
        # Add more assertions as needed for initialization

    def test_update_change_label(self):
        self.app.update_change_label(10)  # Test update change label functionality

    def tearDown(self):
        self.root.destroy()



