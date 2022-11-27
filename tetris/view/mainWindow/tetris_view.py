from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from ...base.IMainWindow import IMainWindow
from ...UI import tetris_view_ui
from ...viewModel.main_view_model import app_model


class TetrisView(QWidget):
    __lvl: int
    __label: QLabel
    __to_menu_view_button: QPushButton

    def __init__(self, main_window) -> None:
        super().__init__()
        self.__lvl = app_model.complexity
        self.main_window = main_window
        self.main_window.setCentralWidget(self)
        uic.loadUi(tetris_view_ui, self)
        self.__setup_ui(label=self.label, to_menu_view_button=self.toMenuViewButton)
        self.__setup_labels()
        self.__setup_buttons()
        # app_model.on_change("state", lambda state: self.__check_state())

    def __setup_ui(
        self, label: QLabel = None, to_menu_view_button: QPushButton = None
    ) -> None:
        self.__label = label
        self.__to_menu_view_button = to_menu_view_button

    # def __check_state(self):
    #     if app_model != "game":
    #         self.hide()
    #         # self.destroy()
    def __setup_labels(self) -> None:
        self.__label.setText(f"Тетрис! Уровень {self.__lvl}")

    def __setup_buttons(self) -> None:
        self.__to_menu_view_button.clicked.connect(lambda: self.__on_menu_select())

    def __on_menu_select(self):
        app_model.state = "menu"


# class TetrisView(QWidget):
#     __lvl: int
#     __main_window: IMainWindow
#     __label: QLabel
#     __to_menu_view_button: QPushButton
#
#     def __init__(self, main_window: IMainWindow = None, lvl: int = 1) -> None:
#         super().__init__()
#         self.__lvl = lvl
#         self.__main_window = main_window
#         uic.loadUi(tetris_view_ui, self)
#         self.__setup_ui(label=self.label, to_menu_view_button=self.toMenuViewButton)
#         self.__setup_labels()
#         self.__setup_buttons()
#
#     def __setup_ui(
#         self, label: QLabel = None, to_menu_view_button: QPushButton = None
#     ) -> None:
#         self.__label = label
#         self.__to_menu_view_button = to_menu_view_button
#
#     def __setup_labels(self) -> None:
#         self.__label.setText(f"Тетрис! Уровень {self.__lvl}")
#
#     def __setup_buttons(self) -> None:
#         self.__to_menu_view_button.clicked.connect(self.__to_menu_view)
#
#     def __to_menu_view(self) -> None:
#         self.__main_window.go_to_previous_view()
#         self.__main_window.remove_main_view(self)
