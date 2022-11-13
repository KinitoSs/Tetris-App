from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog
from base.IMainWindow import IMainWindow
from view.tetris_view import TetrisView


class MenuView(QWidget):
    def __init__(self, main_window: IMainWindow = None) -> None:
        super().__init__()
        self.main_window = main_window
        uic.loadUi("UI/menu_view.ui", self)
        self.__setup_buttons()
        
    def __setup_buttons(self):
        self.toTetrisViewButton.clicked.connect(self.to_tetris_view)
    
    def to_tetris_view(self):
        tetris_view = TetrisView(self.main_window)
        self.main_window.add_main_view(tetris_view)
        self.main_window.go_to_next_main_view()
