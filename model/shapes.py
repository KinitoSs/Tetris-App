import random
from model.figure import Figure


S = [
    [".....", ".....", "..00.", ".00..", "....."],
    [".....", "..0..", "..00.", "...0.", "....."],
]
Z = [
    [".....", ".....", ".00..", "..00.", "....."],
    [".....", "..0..", ".00..", ".0...", "....."],
]
I = [
    ["..0..", "..0..", "..0..", "..0..", "....."],
    [".....", "0000.", ".....", ".....", "....."],
]
O = [[".....", ".....", ".00..", ".00..", "....."]]
J = [
    [".....", ".0...", ".000.", ".....", "....."],
    [".....", "..00.", "..0..", "..0..", "....."],
    [".....", ".....", ".000.", "...0.", "....."],
    [".....", "..0..", "..0..", ".00..", "....."],
]
L = [
    [".....", "...0.", ".000.", ".....", "....."],
    [".....", "..0..", "..0..", "..00.", "....."],
    [".....", ".....", ".000.", ".0...", "....."],
    [".....", ".00..", "..0..", "..0..", "....."],
]
T = [
    [".....", "..0..", ".000.", ".....", "....."],
    [".....", "..0..", "..00.", "..0..", "....."],
    [".....", ".....", ".000.", "..0..", "....."],
    [".....", "..0..", ".00..", "..0..", "....."],
]
shapes = [S, Z, I, O, J, L, T]


def createField(locked_pos={}):
    board = [[0 for _ in range(15)] for _ in range(20)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                board[i][j] = c
    return board


def getShape():
    return Figure(7, 1, random.choice(shapes))


def convertShapeFormat(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions


def validSpace(shape, board):
    accepted_pos = [[(j, i) for j in range(15) if board[i][j] == 0] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convertShapeFormat(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def checkLost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def tryRotate(current_piece, board):
    current_piece.rotation += 1
    if not (validSpace(current_piece, board)):
        current_piece.rotation -= 1


def tryMoveLeft(current_piece, board):
    current_piece.x -= 1
    if not (validSpace(current_piece, board)):
        current_piece.x += 1


def tryMoveRight(current_piece, board):
    current_piece.x += 1
    if not (validSpace(current_piece, board)):
        current_piece.x -= 1


def tryMoveDown(current_piece, board):
    current_piece.y += 1
    if not (validSpace(current_piece, board)):
        current_piece.y -= 1


def clearRows(board, locked, self):
    global score
    inc = 0
    for i in range(len(board) - 1, -1, -1):
        row = board[i]
        if 0 not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    score_map = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}
    score += score_map[inc]
    self.scoreText.setText("Score : " + str(score))


def checkLevel(time):
    time = time // 20
    level = 6
    if time < 60:
        level = 6
    elif time < 120:
        level = 5
    elif time < 180:
        level = 4
    elif time < 360:
        level = 3
    elif time < 600:
        level = 2
    else:
        level = 1
    return level
