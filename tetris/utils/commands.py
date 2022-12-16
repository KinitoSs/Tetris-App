from PyQt5.QtWidgets import QMainWindow

from tetris.base.ICommand import ICommand
from ..model.bricks import block_factory, brick
from ..model.score_handler import score_handler
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


class GetRandomBlockCommand(ICommand):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def execute(self) -> brick.Brick:
        return block_factory.BlockFactory.get_random_block(self.__x, self.__y)


class SaveScoreCommand(ICommand):
    def __init__(self, score):
        self.__score = score

    def execute(self) -> None:
        score_handler.update_score(self.__score)


class GetRecordCommand(ICommand):
    def execute(self) -> int:
        return score_handler.get_record_score()


class GetLastScoreCommand(ICommand):
    def execute(self) -> None:
        return score_handler.get_last_score()
