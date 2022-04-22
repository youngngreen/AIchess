from board.cell import Cell
from pieces.nullpiece import nullpiece
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.bishop import bishop
from pieces.king import king
from pieces.knight import knight
class board:

    gameCells = [[0 for x in range(8)] for y in range(8)]

    def __init__(self):

        pass
    def createboard(self):
        count=0
        for rows in range(8):
            for column in range(8):
                self.gameCells[rows][column] = Cell(count,nullpiece())
                count=count+1

            self.gameCells[0][0] = Cell(0, rook("Black", 0))
            self.gameCells[0][1] = Cell(1, knight("Black", 1))
            self.gameCells[0][2] = Cell(2, bishop("Black", 2))
            self.gameCells[0][3] = Cell(3, queen("Black", 3))
            self.gameCells[0][4] = Cell(4, king("Black", 4))
            self.gameCells[0][5] = Cell(5, bishop("Black", 5))
            self.gameCells[0][6] = Cell(6, knight("Black", 6))
            self.gameCells[0][7] = Cell(7, rook("Black", 7))
            self.gameCells[1][0] = Cell(8, pawn("Black", 8))
            self.gameCells[1][1] = Cell(9, pawn("Black", 9))
            self.gameCells[1][2] = Cell(10, pawn("Black", 10))
            self.gameCells[1][3] = Cell(11, pawn("Black", 11))
            self.gameCells[1][4] = Cell(12, pawn("Black", 12))
            self.gameCells[1][5] = Cell(13, pawn("Black", 13))
            self.gameCells[1][6] = Cell(14, pawn("Black", 14))
            self.gameCells[1][7] = Cell(15, pawn("Black", 15))

            self.gameCells[6][0] = Cell(48, pawn("White", 48))
            self.gameCells[6][1] = Cell(49, pawn("White", 49))
            self.gameCells[6][2] = Cell(50, pawn("White", 50))
            self.gameCells[6][3] = Cell(51, pawn("White", 51))
            self.gameCells[6][4] = Cell(52, pawn("White", 52))
            self.gameCells[6][5] = Cell(53, pawn("White", 53))
            self.gameCells[6][6] = Cell(54, pawn("White", 54))
            self.gameCells[6][7] = Cell(55, pawn("White", 55))
            self.gameCells[7][0] = Cell(56, rook("White", 56))
            self.gameCells[7][1] = Cell(57, knight("White", 57))
            self.gameCells[7][2] = Cell(58, bishop("White", 58))
            self.gameCells[7][3] = Cell(59, queen("White", 59))
            self.gameCells[7][4] = Cell(60, king("White", 60))
            self.gameCells[7][5] = Cell(61, bishop("White", 61))
            self.gameCells[7][6] = Cell(62, knight("White", 62))
            self.gameCells[7][7] = Cell(63, rook("White", 63))

    def printboard(self):
        count = 0
        for rows in range(8):
            for column in range(8):
                print('|', end=self.gameCells[rows][column].pieceonCell.tostring())
            print("|",end='\n')
