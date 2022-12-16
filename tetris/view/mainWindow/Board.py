from ...model.bricks import brick
from ...utils.commands import GetRandomBlockCommand


class Board:
    current_block = ...  # type: brick.Brick
    width: int
    height: int

    new_block_x: float
    new_block_y: float

    def __init__(self, lvl):
        if lvl == 1:
            self.width = 10
            self.height = 20
        elif lvl == 2:
            self.width = 20
            self.height = 30
        elif lvl == 3:
            self.width = 30
            self.height = 40

        self.new_block_x = self.width / 2 - 1
        self.new_block_y = 0

        self.data = [[0] * self.width for _ in range(self.height)]
        self.current_block = None

    def try_insert_random_block(self):
        self.current_block = GetRandomBlockCommand(
            self.new_block_x, self.new_block_y
        ).execute()

        for pt in self.current_block.get_coords():
            if pt[0] >= 0 and pt[1] >= 0:  # blocks may be created at negative pos
                if self.data[pt[1]][pt[0]] != 0:
                    return False
        print("Inserted ", self.current_block.get_name())
        return True

    def can_move_current_block(self, x_offset, y_offset):
        coords = self.current_block.peek_coords(x_offset, y_offset)
        return all(
            0 <= x < self.width and 0 <= y < self.height for x, y in coords
        ) and all(self.data[j][i] == 0 for i, j in coords)

    def can_rotate_current_block(self, direction):
        """Направление: 1 направо 2 налево"""
        coords = self.current_block.peek_rotated_coords(direction)
        return all(
            0 <= x < self.width and 0 <= y < self.height for x, y in coords
        ) and all(self.data[j][i] == 0 for i, j in coords)

    def permanently_insert_current_block(self):
        for pt in self.current_block.get_coords():
            self.data[pt[1]][pt[0]] = 1

    def remove_full_rows(self) -> int:
        """Возвращает количество удаленных строк (0, если они any)."""
        rows_removed = 0
        for row in range(0, self.height):
            if all(self.data[row][col] for col in range(0, self.width)):
                rows_removed = rows_removed + 1
                for row1 in range(row, 0, -1):  # y axis goes down
                    self.__copy_row(row1 - 1, row1)
                self.__clear_row(0)
        return rows_removed

    def remove_all(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] = 0

    def __copy_row(self, src_row_index, target_row_index):
        for i in range(0, self.width):
            self.data[target_row_index][i] = self.data[src_row_index][i]

    def __clear_row(self, row_index):
        for i in range(0, self.width):
            self.data[row_index][i] = 0
