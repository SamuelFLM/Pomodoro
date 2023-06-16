import unittest
from unittest.mock import patch, MagicMock
import PySimpleGUI as sg
from app.interface_home import Home  # Substitua "sua_classe" pelo nome do módulo ou arquivo que contém a classe


class TestSuaClasse(unittest.TestCase):

    def setUp(self) -> None:
        self.home = Home()

    def test_init(self):
        self.assertEqual(self.home.background_color, sg.theme_background_color("#C6E59D"))

    def test_front(self):
        with patch('PySimpleGUI.Window') as mock_window:
            home = Home()
            window = home.front()
            mock_window.assert_called_with("Sessão de foco", layout=unittest.mock.ANY, size=(272, 442), margins=(0, 0),
                                           grab_anywhere=True,
                                           element_justification='c', icon="dependency//img//ico.ico")

    def test_back(self):
        with patch('builtins.print') as mock_print:
            home = Home()
            window = MagicMock()
            window.read = MagicMock(return_value=(sg.WIN_CLOSED, None))
            home.back(window)
            mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
