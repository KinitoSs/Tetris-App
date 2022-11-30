from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from ...UI import tetris_view_ui
from ...viewModel.main_view_model import app_model


class TetrisView(QWidget):
    def __init__(self, main_window) -> None:
        super().__init__()
        self.__lvl = app_model.complexity
        self.main_window = main_window

        self.main_window.setCentralWidget(self)
        uic.loadUi(tetris_view_ui, self)
        self.__setup_buttons()

    def __setup_buttons(self) -> None:
        self.toMenuViewButton.clicked.connect(lambda: app_model.set_state("menu"))
