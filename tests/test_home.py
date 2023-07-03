import unittest
from unittest.mock import patch, MagicMock
import PySimpleGUI as sg
from app.interface_home import InterfaceHome  # Substitua "sua_classe" pelo nome do módulo ou arquivo que contém a classe


class TestSuaClasse(unittest.TestCase):

    def setUp(self) -> None:
        self.home = InterfaceHome()

    def test_init(self):
        self.assertEqual(self.home.background_color, sg.theme_background_color("#C6E59D"))


if __name__ == '__main__':
    unittest.main()
