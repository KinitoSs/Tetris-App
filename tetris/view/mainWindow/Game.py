from PyQt5.QtCore import QBasicTimer, pyqtSignal, QObject

from tetris.utils.commands import ShowMessageCommand, SaveScoreCommand
from tetris.viewModel.main_view_model import app_model


class Game(QObject):
    # must be static
    board_updated = pyqtSignal()
    status_updated = pyqtSignal(str)
    score_updated = pyqtSignal(int)
    level_updated = pyqtSignal(int)

    points_for_single_block = 20
    points_for_row_cleared = 100
    points_for_level_up = 400  # после получения n очков ** уровня, уровень повышается
    base_speed = 320  # интервал обновления для уровня 1
    speed_decrement = 20  # декремент таймера для каждого уровня
    high_speed = 50  # интервал таймера при нажатии пробела

    def __init__(self, board):
        super().__init__()
        self.__board = board
        self.__timer = QBasicTimer()
        self.__speed = self.base_speed
        self.__speedBackup = self.__speed
        self.__highSpeedMode = False
        self.__score = 0
        self.__level = 1
        self.__status = ""
        self.__game_over = False
        self.new_game()

    def start(self):
        if not self.__game_over:
            self.__timer.start(self.__speed, self)

    def stop(self):
        self.__timer.stop()

    def __change_speed(self, speed):
        self.__speed = speed
        if self.__timer.isActive():
            self.start()

    def __add_points(self, added):
        """Обновляет очки и скорость.
        Количество добавленных очков зависит от уровня"""
        added = added * self.__level
        self.__score = self.__score + added
        self.score_updated.emit(self.__score)
        self.unset_high_speed()
        if (
            self.__score > self.__number_of_points_to_change_level()
            and self.__speed - self.speed_decrement > 0
        ):
            self.__level = self.__level + 1
            self.level_updated.emit(self.__level)
            self.__change_speed(self.__speed - self.speed_decrement)

    def __number_of_points_to_change_level(self):
        return self.points_for_level_up**self.__level

    def __change_status_message(self, msg):
        self.__status = msg
        self.status_updated.emit(msg)

    def timerEvent(self, event):
        if event.timerId() == self.__timer.timerId():
            if self.__board.can_move_current_block(0, 1):
                self.__board.current_block.move_down()
            else:
                self.__board.permanently_insert_current_block()
                self.__add_points(self.points_for_single_block)
                rows_removed = self.__board.remove_full_rows()
                self.__add_points(self.points_for_row_cleared * rows_removed)
                if not self.__board.try_insert_random_block():
                    self.__game_over = True
                    self.stop()
                    self.__change_status_message("Game over!")
                    SaveScoreCommand(self.__score, app_model.complexity).execute()
                    app_model.state = "results"
            self.board_updated.emit()

    def get_status(self) -> str:
        return self.__status

    def get_score(self) -> int:
        return self.__score

    def get_level(self) -> int:
        return self.__level

    def set_high_speed(self):
        if not self.__highSpeedMode:
            self.__highSpeedMode = True
            self.__speedBackup = self.__speed
            self.__change_speed(self.high_speed)

    def unset_high_speed(self):
        if self.__highSpeedMode:
            self.__change_speed(self.__speedBackup)
            self.__highSpeedMode = False

    def toggle_pause(self):
        if not self.__game_over:
            if self.__timer.isActive():
                self.__change_status_message("Paused")
                self.stop()
            else:
                self.start()
                self.__change_status_message("")

    def new_game(self):
        self.stop()
        self.__speed = self.base_speed
        self.__speedBackup = self.__speed
        self.__highSpeedMode = False
        self.__score = 0
        self.__level = 1
        self.__game_over = False
        self.score_updated.emit(self.__score)
        self.level_updated.emit(self.__level)
        self.__change_status_message("")
        self.__board.remove_all()
        self.__board.insert_obstacle()
        self.__board.try_insert_random_block()
        self.board_updated.emit()
