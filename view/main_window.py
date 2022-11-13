from PyQt5.QtWidgets import (
    QDesktopWidget,
    QStackedWidget,
    QWidget,
)
from base.IMainWindow import IMainWindow
from view.menu_view import MenuView
from view.tetris_view import TetrisView
from PyQt5 import uic


class MainWindow(IMainWindow):
    main_view: QStackedWidget

    def __init__(self) -> None:
        super().__init__()
        self.__setup_ui()

    def __setup_ui(self) -> None:
        uic.loadUi("UI/main_window.ui", self)

        self.main_view = QStackedWidget()
        self.main_view.addWidget(MenuView(self))

        self.setCentralWidget(self.main_view)

        self.__center()
        self.show()

    def __center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
        )

    def add_main_view(self, view: QWidget):
        self.main_view.addWidget(view)

    def remove_main_view(self, view: QWidget):
        self.main_view.removeWidget(view)

    def go_to_next_main_view(self):
        self.main_view.setCurrentIndex(self.main_view.currentIndex() + 1)

    def go_to_previous_view(self):
        self.main_view.setCurrentIndex(self.main_view.currentIndex() - 1)
