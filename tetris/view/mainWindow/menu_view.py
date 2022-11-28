from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton
from ...base.IMainWindow import IMainWindow
from .tetris_view import TetrisView
from ...UI import menu_view_ui
from ...viewModel.main_view_model import app_model


class MenuView(QWidget):
    def __init__(self, main_window) -> None:
        super().__init__()
        self.main_window = main_window
        self.main_window.setCentralWidget(self)
        uic.loadUi(menu_view_ui, self)
        self.__setup_buttons()

    def __setup_buttons(self):
        self.toTetris1ViewButton.clicked.connect(lambda: self.__on_level_select(1))
        self.toTetris2ViewButton.clicked.connect(lambda: self.__on_level_select(2))
        self.toTetris3ViewButton.clicked.connect(lambda: self.__on_level_select(3))

    def __on_level_select(self, lvl: int):
        app_model.complexity = lvl
        app_model.state = "game"
