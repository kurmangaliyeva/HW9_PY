import random
from Classes import Board


def AIMove(field: Board):
    my_mark = field.getMark()
    en_Mark = field.getEnemyMark()
    win = field.getWin()
    board = field.getBoard()
    if board[4].isdigit():
        return 4
    for pos in win:
        if (board[pos[0]] == board[pos[1]] == my_mark) and board[pos[2]].isdigit():
            return int(pos[2])
        elif (board[pos[0]] == board[pos[2]] == my_mark) and board[pos[1]].isdigit():
            return int(pos[1])
        elif (board[pos[1]] == board[pos[2]] == my_mark) and board[pos[0]].isdigit():
            return int(pos[0])
    for pos in win:
        if (board[pos[0]] == board[pos[1]] == en_Mark) and board[pos[2]].isdigit():
            return int(pos[2])
        elif (board[pos[0]] == board[pos[2]] == en_Mark) and board[pos[1]].isdigit():
            return int(pos[1])
        elif (board[pos[1]] == board[pos[2]] == en_Mark) and board[pos[0]].isdigit():
            return int(pos[0])
    corner = [0,2,6,8]
    random.shuffle(corner)
    for pos in corner:
        if board[pos].isdigit():
            return int(pos)
    while True:
        move = random.randint(0,8)
        if (0 <= move <= 8) and board[move].isdigit():
            return move
