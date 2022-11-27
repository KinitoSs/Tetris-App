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
        self.__setup_ui(
            to_tetris_1_view_button=self.toTetris1ViewButton,
            to_tetris_2_view_button=self.toTetris2ViewButton,
            to_tetris_3_view_button=self.toTetris3ViewButton,
        )
        self.__setup_buttons()
        # app_model.on_change("state", lambda state: self.__check_state())

    # def __check_state(self):
    #     if app_model.state != "menu":
    #         self.hide()
    #         # self.destroy()

    def __setup_ui(
        self,
        to_tetris_1_view_button: QPushButton = None,
        to_tetris_2_view_button: QPushButton = None,
        to_tetris_3_view_button: QPushButton = None,
    ):
        self.__to_tetris_1_view_button = to_tetris_1_view_button
        self.__to_tetris_2_view_button = to_tetris_2_view_button
        self.__to_tetris_3_view_button = to_tetris_3_view_button

    def __setup_buttons(self):
        self.__to_tetris_1_view_button.clicked.connect(
            lambda: self.__on_level_select(1)
        )
        self.__to_tetris_2_view_button.clicked.connect(
            lambda: self.__on_level_select(2)
        )
        self.__to_tetris_3_view_button.clicked.connect(
            lambda: self.__on_level_select(3)
        )

    def __on_level_select(self, lvl: int):
        app_model.complexity = lvl
        app_model.state = "game"


# class MenuView(QWidget):
#     __to_tetris_1_view_button: QPushButton
#     __to_tetris_2_view_button: QPushButton
#     __to_tetris_3_view_button: QPushButton
#
#     def __init__(self, main_window: IMainWindow = None) -> None:
#         super().__init__()
#         self.main_window = main_window
#         uic.loadUi(menu_view_ui, self)
#         self.__setup_ui(
#             to_tetris_1_view_button=self.toTetris1ViewButton,
#             to_tetris_2_view_button=self.toTetris2ViewButton,
#             to_tetris_3_view_button=self.toTetris3ViewButton,
#         )
#         self.__setup_buttons()
#
#     def __setup_ui(
#         self,
#         to_tetris_1_view_button: QPushButton = None,
#         to_tetris_2_view_button: QPushButton = None,
#         to_tetris_3_view_button: QPushButton = None,
#     ):
#         self.__to_tetris_1_view_button = to_tetris_1_view_button
#         self.__to_tetris_2_view_button = to_tetris_2_view_button
#         self.__to_tetris_3_view_button = to_tetris_3_view_button
#
#     def __setup_buttons(self):
#         self.__to_tetris_1_view_button.clicked.connect(lambda: self.to_tetris_view(1))
#         self.__to_tetris_2_view_button.clicked.connect(lambda: self.to_tetris_view(2))
#         self.__to_tetris_3_view_button.clicked.connect(lambda: self.to_tetris_view(3))
#
#     def to_tetris_view(self, lvl: int):
#         tetris_view = TetrisView(main_window=self.main_window, lvl=lvl)
#         self.main_window.add_main_view(tetris_view)
#         self.main_window.go_to_next_main_view()
