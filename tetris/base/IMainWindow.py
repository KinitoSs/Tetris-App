from PyQt5.QtWidgets import QWidget, QMainWindow


class IMainWindow(QMainWindow):
    def add_main_view(self, view: QWidget) -> None:
        raise NotImplementedError

    def remove_main_view(self, view: QWidget) -> None:
        raise NotImplementedError

    def go_to_next_main_view(self) -> None:
        raise NotImplementedError

    def go_to_previous_view(self) -> None:
        raise NotImplementedError
