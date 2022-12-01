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
        self.__lvl = app_model.complexity
        self.main_window = main_window

        self.main_window.setCentralWidget(self)
        uic.loadUi(tetris_view_ui, self)
        self.__setup_buttons()

        self._board = Board()
        self._game = Game(self._board)
        self.initialize_ui()
        self._game.start()

    def initialize_ui(self):
        qgv = QGraphicsView(self)
        self._scene = QGraphicsScene(qgv)
        qgv.setScene(self._scene)
        self.verticalLayout: QVBoxLayout
        self.verticalLayout.addWidget(qgv)
        # self.main_window.resize(self._board.Width * self.BrickSize + self.Margin,
        #                         self._board.Height * self.BrickSize + self.Margin)
        self._scene.setSceneRect(0, 0, self._board.Width * self.BrickSize, self._board.Height * self.BrickSize)
        # self.center_on_screen()
        self.draw_board()
        self._game.boardUpdated.connect(self.draw_board)

        # self._game.scoreUpdated.connect(self.update_status)
        # self._game.levelUpdated.connect(self.update_status)
        # self._game.statusUpdated.connect(self.update_status)

        # self.setWindowTitle("PyTris")

        # self.update_status()

    def draw_board(self):
        self._scene.clear()
        self._scene.addRect(self._scene.sceneRect(), QPen(Qt.lightGray))
        for point in self._board.current_block.get_coords():
            self._scene.addRect(point[0] * self.BrickSize, point[1] * self.BrickSize, self.BrickSize, self.BrickSize)
        for i in range(0, self._board.Width):
            for j in range(0, self._board.Height):
                if self._board.data[j][i] != 0:
                    self._scene.addRect(i * self.BrickSize, j * self.BrickSize, self.BrickSize,
                                        self.BrickSize, QPen(Qt.lightGray), QBrush(Qt.gray))

    # def update_status(self):
    #     self._statusbar.showMessage("{} Score: {} Level: {}".format(self._game.get_status(), self._game.get_score(),
    #                                                                 self._game.get_level()))

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_W:
            if self._board.can_rotate_current_block(-1):
                self._board.current_block.rotate_left()
        elif key == Qt.Key_S:
            if self._board.can_rotate_current_block(1):
                self._board.current_block.rotate_right()
        elif key == Qt.Key_A:
            if self._board.can_move_current_block(-1, 0):
                self._board.current_block.move_left()
        elif key == Qt.Key_D:
            if self._board.can_move_current_block(1, 0):
                self._board.current_block.move_right()
        elif key == Qt.Key_Space:
            self._game.set_high_speed()
        elif key == Qt.Key_P:
            self._game.toggle_pause()
        elif key == Qt.Key_N:
            self._game.new_game()
            self._game.start()

    def keyReleaseEvent(self, e):
        self._game.unset_high_speed()

    def __setup_buttons(self) -> None:
        self.toMenuViewButton.clicked.connect(lambda: app_model.set_state("menu"))
