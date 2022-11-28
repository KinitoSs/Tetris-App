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

        self.__setup_menu_actions()

        self.__center()
        self.__current_view = MenuView(self)
        self.setCentralWidget(self.__current_view)
        self.show()

    def __check_state(self):
        if app_model.state == "menu":
            self.__current_view = MenuView(self)
        elif app_model.state == "game":
            self.__current_view = TetrisView(self)

    def __setup_menu_actions(self):
        self.menuExitAction.triggered.connect(self.__exit_action)
        self.menuAboutProgramAction.triggered.connect(self.__about_programm_action)

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
