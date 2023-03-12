class Board:
    board = ['1','2','3','4','5','6','7','8','9']
    MARK = None
    win = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
                (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    def __init__(self, settings):
        self.MARK = settings.get('PLAYER_MARK')

    def new_game(self, settings):
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.MARK = settings.get('PLAYER_MARK')

    def getField(self):
        return self.board

    def getMark(self) -> str:
        return self.MARK

    def setMark(self, mark):
        self.MARK = mark

    def getEnemyMark(self):
        if self.MARK == 'O':
            return 'X'
        else:
            return 'O'

    def changeMark(self):
        if self.MARK == 'O':
            self.MARK = 'X'
        else:
            self.MARK = 'O'

    def getBoard(self):
        return self.board

    def setBoard(self, index):
        self.board[index] = self.getMark()


    def getWin(self):
        return self.win

    def win_condition(self):
        for move in self.win:
            if self.board[move[0]] == self.board[move[1]] == self.board[move[2]]:
                return move

    def check_tie(self):
        if len(set(self.board)) == 2:
            return True