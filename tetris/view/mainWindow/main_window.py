from PyQt5.QtWidgets import (
    QDesktopWidget,
    QStackedWidget,
    QWidget,
    QMenu,
    QAction,
    QMainWindow,
)
from ...base.IMainWindow import IMainWindow
from .menu_view import MenuView, TetrisView
from PyQt5 import uic
from .message_view import MessageView
from ...UI import main_window_ui
from ...viewModel.main_view_model import app_model


class MainWindow(QMainWindow):
    __current_view: QWidget

    def __init__(self) -> None:
        super().__init__()
        app_model.on_change("state", lambda state: self.__check_state())
        uic.loadUi(main_window_ui, self)
        self.__setup_ui(
            menu_file=self.menuFile,
            menu_help=self.menuHelp,
            menu_exit_action=self.menuExitAction,
            menu_about_programm_action=self.menuAboutProgrammAction,
        )

        self.__setup_menu_actions()

        # self.__center()
        self.__current_view = MenuView(self)
        self.setCentralWidget(self.__current_view)
        self.show()

    def __setup_ui(
        self,
        menu_file: QMenu = None,
        menu_help: QMenu = None,
        menu_exit_action: QAction = None,
        menu_about_programm_action: QAction = None,
    ):
        self.__menu_file = menu_file
        self.__menu_help = menu_help
        self.__menu_exit_action = menu_exit_action
        self.__menu_about_programm_action = menu_about_programm_action

    def __check_state(self):
        if app_model.state == "menu":
            self.__current_view = MenuView(self)
        elif app_model.state == "game":
            self.__current_view = TetrisView(self)

    def __setup_menu_actions(self):
        self.__menu_exit_action.triggered.connect(self.__exit_action)
        self.__menu_about_programm_action.triggered.connect(
            self.__about_programm_action
        )

    def __center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
        )

    def __exit_action(self):
        self.close()

    def __about_programm_action(self):
        MessageView(
            "Выполнил студент САФУ, 3 курс, 351018, \nАрхаров Никита Михайлович."
        ).exec()


# class MainWindow(IMainWindow):
#     main_view: QStackedWidget
#     __menu_file: QMenu
#     __menu_help: QMenu
#     __menu_exit_action: QAction
#     __menu_about_programm_action: QAction
#
#     def __init__(self) -> None:
#         super().__init__()
#
#         uic.loadUi(main_window_ui, self)
#         self.__setup_ui(
#             menu_file=self.menuFile,
#             menu_help=self.menuHelp,
#             menu_exit_action=self.menuExitAction,
#             menu_about_programm_action=self.menuAboutProgrammAction,
#         )
#
#         self.__setup_menu_actions()
#
#         self.main_view = QStackedWidget()
#         self.main_view.addWidget(MenuView(self))
#
#         self.setCentralWidget(self.main_view)
#
#         self.__center()
#         self.show()
#
#     def __setup_ui(
#         self,
#         menu_file: QMenu = None,
#         menu_help: QMenu = None,
#         menu_exit_action: QAction = None,
#         menu_about_programm_action: QAction = None,
#     ):
#         self.__menu_file = menu_file
#         self.__menu_help = menu_help
#         self.__menu_exit_action = menu_exit_action
#         self.__menu_about_programm_action = menu_about_programm_action
#
#     def __setup_menu_actions(self):
#         self.__menu_exit_action.triggered.connect(self.__exit_action)
#         self.__menu_about_programm_action.triggered.connect(
#             self.__about_programm_action
#         )
#
#     def __center(self):
#         screen = QDesktopWidget().screenGeometry()
#         size = self.geometry()
#         self.move(
#             (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
#         )
#
#     def __exit_action(self):
#         self.close()
#
#     def __about_programm_action(self):
#         MessageView(
#             "Выполнил студент САФУ, 3 курс, 351018, \nАрхаров Никита Михайлович."
#         ).exec()
#
#     def add_main_view(self, view: QWidget):
#         self.main_view.addWidget(view)
#
#     def remove_main_view(self, view: QWidget):
#         self.main_view.removeWidget(view)
#
#     def go_to_next_main_view(self):
#         self.main_view.setCurrentIndex(self.main_view.currentIndex() + 1)
#
#     def go_to_previous_view(self):
#         self.main_view.setCurrentIndex(self.main_view.currentIndex() - 1)
