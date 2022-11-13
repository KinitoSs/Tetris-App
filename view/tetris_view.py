from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from base.IMainWindow import IMainWindow


class TetrisView(QWidget):
    def __init__(self, main_window: IMainWindow = None) -> None:
        super().__init__()
        self.main_window = main_window
        uic.loadUi("UI/tetris_view.ui", self)
        self.toMenuViewButton.clicked.connect(self.to_menu_view)

    def to_menu_view(self):
        self.main_window.go_to_previous_view()
        self.main_window.remove_main_view(self)
