"""
1. Game
2. Pieces
3. Board
4. Box
5. Players

"""


class Pieces:
    def __init__(self):
        pass


class King(Pieces):
    pass


class Queen(Pieces):
    pass


class Bishops(Pieces):
    pass


class Knight(Pieces):
    pass


class Rook(Pieces):
    pass


class Pawn(Pieces):
    pass


class Board:
    pass


class Players:
    pass


class Game:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.player = Players()
