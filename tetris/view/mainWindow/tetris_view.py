from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QVBoxLayout

from .Board import Board
from .Game import Game
from ...UI import tetris_view_ui
from ...viewModel.main_view_model import app_model


class TetrisView(QWidget):
    BrickSize: int = 15
    Margin = 50

    def __init__(self, main_window) -> None:
        super().__init__()
        self.pauseButton = None
        self.toMenuViewButton = None
        self.verticalLayout = None
        self.__scene = None
        self.__lvl = app_model.complexity
        self.main_window = main_window
        self.__status_bar = self.main_window.statusBar()

        self.main_window.setCentralWidget(self)
        uic.loadUi(tetris_view_ui, self)

        self.__board = Board(self.__lvl)
        self.__game = Game(self.__board)
        self.initialize_ui()
        self.__game.start()
        self.__setup_buttons()

    def initialize_ui(self):
        qgv = QGraphicsView(self)
        self.__scene = QGraphicsScene(qgv)
        qgv.setScene(self.__scene)
        self.verticalLayout: QVBoxLayout
        self.verticalLayout.addWidget(qgv)

        # self.main_window.resize(
        #     self.__board.width * self.BrickSize + self.Margin,
        #     (self.__board.height + 5) * self.BrickSize + self.Margin,
        # )

        self.__scene.setSceneRect(
            0,
            0,
            self.__board.width * self.BrickSize,
            self.__board.height * self.BrickSize,
        )

        self.draw_board()

        self.__game.board_updated.connect(self.draw_board)
        self.__game.score_updated.connect(self.update_status)
        self.__game.level_updated.connect(self.update_status)
        self.__game.status_updated.connect(self.update_status)

        self.update_status()

    def draw_board(self):
        self.__scene.clear()
        self.__scene.addRect(self.__scene.sceneRect(), QPen(Qt.lightGray))
        for point in self.__board.current_block.get_coords():
            self.__scene.addRect(
                point[0] * self.BrickSize,
                point[1] * self.BrickSize,
                self.BrickSize,
                self.BrickSize,
            )
        for i in range(0, self.__board.width):
            for j in range(0, self.__board.height):
                if self.__board.data[j][i] != 0:
                    self.__scene.addRect(
                        i * self.BrickSize,
                        j * self.BrickSize,
                        self.BrickSize,
                        self.BrickSize,
                        QPen(Qt.lightGray),
                        QBrush(Qt.green),
                    )

    def update_status(self):
        self.__status_bar.showMessage(
            "{} Score: {} Level: {}".format(
                self.__game.get_status(),
                self.__game.get_score(),
                self.__game.get_level(),
            )
        )

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_W:
            if self.__board.can_rotate_current_block(-1):
                self.__board.current_block.rotate_left()
        elif key == Qt.Key_S:
            if self.__board.can_rotate_current_block(1):
                self.__board.current_block.rotate_right()
        elif key == Qt.Key_A:
            if self.__board.can_move_current_block(-1, 0):
                self.__board.current_block.move_left()
        elif key == Qt.Key_D:
            if self.__board.can_move_current_block(1, 0):
                self.__board.current_block.move_right()
        elif key == Qt.Key_Space:
            self.__game.set_high_speed()
        elif key == Qt.Key_N:
            self.__game.new_game()
            self.__game.start()

    def keyReleaseEvent(self, e):
        self.__game.unset_high_speed()

    def __setup_buttons(self) -> None:
        self.toMenuViewButton.clicked.connect(lambda: app_model.set_state("menu"))
        self.pauseButton.clicked.connect(lambda: self.__game.toggle_pause())
