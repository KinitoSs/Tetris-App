from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from base.IMainWindow import IMainWindow


class TetrisView(QWidget):
    __lvl: int
    __main_window: IMainWindow
    __label: QLabel
    __to_menu_view_button: QPushButton

    def __init__(self, main_window: IMainWindow = None, lvl: int = 1) -> None:
        super().__init__()
        self.__lvl = lvl
        self.__main_window = main_window
        uic.loadUi("UI/tetris_view.ui", self)
        self.__setup_ui(label=self.label, to_menu_view_button=self.toMenuViewButton)
        self.__setup_labels()
        self.__setup_buttons()

    def __setup_ui(
        self, label: QLabel = None, to_menu_view_button: QPushButton = None
    ) -> None:
        self.__label = label
        self.__to_menu_view_button = to_menu_view_button

    def __setup_labels(self) -> None:
        self.__label.setText(f"Тетрис! Уровень {self.__lvl}")

    def __setup_buttons(self) -> None:
        self.__to_menu_view_button.clicked.connect(self.__to_menu_view)

    def __to_menu_view(self) -> None:
        self.__main_window.go_to_previous_view()
        self.__main_window.remove_main_view(self)
