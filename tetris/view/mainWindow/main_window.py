from PyQt5 import uic
from PyQt5.QtWidgets import (
    QDesktopWidget,
    QWidget,
    QMainWindow,
)

from .menu_view import MenuView
from .tetris_view import TetrisView
from ...UI import main_window_ui
from ...utils.commands import ExitCommand, ShowMessageCommand
from ...viewModel.main_view_model import app_model


class MainWindow(QMainWindow):
    __current_view: QWidget

    def __init__(self) -> None:
        super().__init__()

        app_model.on_change("state", lambda state: self.__check_state())
        app_model.on_change("command", lambda command: self.__check_command())

        uic.loadUi(main_window_ui, self)

        self.__setup_menu_actions()

        self.__current_view = MenuView(self)
        self.setCentralWidget(self.__current_view)

        self.__center()
        self.show()

    def __setup_menu_actions(self):
        self.menuExitAction.triggered.connect(lambda: app_model.set_command("exit"))
        self.menuAboutProgramAction.triggered.connect(
            lambda: app_model.set_command("about_programm")
        )

    def __center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
        )

    def __check_state(self):
        if app_model.state == "menu":
            self.__current_view = MenuView(self)
        elif app_model.state == "game":
            self.__current_view = TetrisView(self)

    def __check_command(self):
        if app_model.command == "exit":
            ExitCommand(self).execute()

        elif app_model.command == "about_programm":
            ShowMessageCommand(
                "Выполнил студент САФУ, 3 курс, 351018, \nАрхаров Никита Михайлович."
            ).execute()
