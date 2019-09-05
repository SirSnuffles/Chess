import Pieces


class Board:
    def __init__(self):
        self.BoardArray = [[Pieces.Piece("White") for x in range(8)] for y in range(8)]
        wRook1 = Pieces.Rook((0, 0), "White", "Black")
        wRook2 = Pieces.Rook((7, 0), "White", "White")
        wKnight1 = Pieces.Knight((1, 0), "White", "White")
        wKnight2 = Pieces.Knight((6, 0), "White", "Black")
        wBishop1 = Pieces.Bishop((2, 0), "White", "Black")
        wBishop2 = Pieces.Bishop((5, 0), "White", "White")
        wQueen1 = Pieces.Queen((3, 0), "White", "White")
        wKing1 = Pieces.King((4, 0), "White", "Black")
        wPawn1 = Pieces.Pawn((0, 1), "White", "White")
        wPawn2 = Pieces.Pawn((1, 1), "White", "Black")
        wPawn3 = Pieces.Pawn((2, 1), "White", "White")
        wPawn4 = Pieces.Pawn((3, 1), "White", "Black")
        wPawn5 = Pieces.Pawn((4, 1), "White", "White")
        wPawn6 = Pieces.Pawn((5, 1), "White", "Black")
        wPawn7 = Pieces.Pawn((6, 1), "White", "White")
        wPawn8 = Pieces.Pawn((7, 1), "White", "Black")

        bRook1 = Pieces.Rook((0, 7), "Black", "White")
        bRook2 = Pieces.Rook((7, 7), "Black", "Black")
        bKnight1 = Pieces.Knight((1, 7), "Black", "Black")
        bKnight2 = Pieces.Knight((6, 7), "Black", "White")
        bBishop1 = Pieces.Bishop((2, 7), "Black", "White")
        bBishop2 = Pieces.Bishop((5, 7), "Black", "Black")
        bQueen1 = Pieces.Queen((3, 7), "Black", "Black")
        bKing1 = Pieces.King((4, 7), "Black", "White")
        bPawn1 = Pieces.Pawn((0, 6), "Black", "Black")
        bPawn2 = Pieces.Pawn((1, 6), "Black", "White")
        bPawn3 = Pieces.Pawn((2, 6), "Black", "Black")
        bPawn4 = Pieces.Pawn((3, 6), "Black", "White")
        bPawn5 = Pieces.Pawn((4, 6), "Black", "Black")
        bPawn6 = Pieces.Pawn((5, 6), "Black", "White")
        bPawn7 = Pieces.Pawn((6, 6), "Black", "Black")
        bPawn8 = Pieces.Pawn((7, 6), "Black", "White")

        self.BoardArray[0][0] = wRook1
        self.BoardArray[0][7] = wRook2
        self.BoardArray[0][1] = wKnight1
        self.BoardArray[0][6] = wKnight2
        self.BoardArray[0][2] = wBishop1
        self.BoardArray[0][5] = wBishop2
        self.BoardArray[0][3] = wQueen1
        self.BoardArray[0][4] = wKing1

        self.BoardArray[1][0] = wPawn1
        self.BoardArray[1][1] = wPawn2
        self.BoardArray[1][2] = wPawn3
        self.BoardArray[1][3] = wPawn4
        self.BoardArray[1][4] = wPawn5
        self.BoardArray[1][5] = wPawn6
        self.BoardArray[1][6] = wPawn7
        self.BoardArray[1][7] = wPawn8

        self.BoardArray[7][0] = bRook1
        self.BoardArray[7][7] = bRook2
        self.BoardArray[7][1] = bKnight1
        self.BoardArray[7][6] = bKnight2
        self.BoardArray[7][2] = bBishop1
        self.BoardArray[7][5] = bBishop2
        self.BoardArray[7][3] = bQueen1
        self.BoardArray[7][4] = bKing1

        self.BoardArray[6][0] = bPawn1
        self.BoardArray[6][1] = bPawn2
        self.BoardArray[6][2] = bPawn3
        self.BoardArray[6][3] = bPawn4
        self.BoardArray[6][4] = bPawn5
        self.BoardArray[6][5] = bPawn6
        self.BoardArray[6][6] = bPawn7
        self.BoardArray[6][7] = bPawn8

    def __repr__(self):
        reprBoard = [[] for i in range(len(self.BoardArray))]
        for rowIndx, row in enumerate(self.BoardArray):
            for item in row:
                reprBoard[rowIndx].append(item.name)
        return reprBoard

    def move(self, piece, pos):
        if pos in Pieces.piece.getPossiblePos():
            print("possible")
        else:
            pass


# def main():
#     newBoard = Board()
#     newBoard.__repr__()
#     for i in newBoard.BoardArray:
#         print(i)


# if __name__ == "__main__":
#     main()
