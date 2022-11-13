import abc
from PyQt5.QtWidgets import QWidget, QMainWindow


class IMainWindow(QMainWindow):
    @abc.abstractmethod
    def add_main_view(self, view: QWidget) -> None:
        pass

    @abc.abstractmethod
    def remove_main_view(self, view: QWidget) -> None:
        pass

    @abc.abstractmethod
    def go_to_next_main_view(self) -> None:
        pass

    @abc.abstractmethod
    def go_to_previous_view(self) -> None:
        pass
