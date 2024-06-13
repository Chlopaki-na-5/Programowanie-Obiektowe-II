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

if __name__ == '__main__':
    unittest.main()
