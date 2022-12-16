from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from ...UI import menu_view_ui
from ...utils.commands import GetRecordCommand, GetLastScoreCommand
from ...viewModel.main_view_model import app_model


class MenuView(QWidget):
    def __init__(self, main_window) -> None:
        super().__init__()
        self.main_window = main_window
        self.main_window.setCentralWidget(self)
        uic.loadUi(menu_view_ui, self)
        self.__setup_buttons()

        self.label: QLabel
        self.label.setText(
            f"Тетрис!\nРекорд: {GetRecordCommand().execute()}\nПоследний счёт: {GetLastScoreCommand().execute()}"
        )

    def __setup_buttons(self):
        self.toTetris1ViewButton: QPushButton
        self.toTetris1ViewButton.clicked.connect(lambda: app_model.set_complexity(1))
        self.toTetris1ViewButton.clicked.connect(lambda: app_model.set_state("game"))

        self.toTetris2ViewButton: QPushButton
        self.toTetris2ViewButton.clicked.connect(lambda: app_model.set_complexity(2))
        self.toTetris2ViewButton.clicked.connect(lambda: app_model.set_state("game"))

        self.toTetris3ViewButton: QPushButton
        self.toTetris3ViewButton.clicked.connect(lambda: app_model.set_complexity(3))
        self.toTetris3ViewButton.clicked.connect(lambda: app_model.set_state("game"))
