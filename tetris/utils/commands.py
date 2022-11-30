from PyQt5.QtWidgets import QMainWindow

from tetris.base.ICommand import ICommand
from ..view.mainWindow.message_view import MessageView


class ExitCommand(ICommand):
    def __init__(self, executor: QMainWindow):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.close()


class ShowMessageCommand(ICommand):
    def __init__(self, message: str):
        self.__message = message

    def execute(self) -> None:
        MessageView(self.__message).exec()
