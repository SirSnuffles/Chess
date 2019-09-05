import gui


class Piece:
    def __init__(self, squareColour):
        self.name = ""
        self.squareColour = squareColour


class Rook(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "Rook"
        self.location = location
        self.colour = colour


class Knight(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "Knight"
        self.location = location
        self.colour = colour


class Bishop(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "Bishop"
        self.location = location
        self.colour = colour


class Queen(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "Queen"
        self.location = location
        self.colour = colour


class King(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "King"
        self.location = location
        self.colour = colour
        self.isChecked = False


class Pawn(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self, squareColour)
        self.name = "Pawn"
        self.location = location
        self.colour = colour
        self.AllowDoubleMove = True


# def main():
#     newPiece = Piece("White")
#     print(newPiece.squareColour)
#     newPawn = Pawn((1, 2), "black", "White")
#     print(newPawn.squareColour)
#     newPawn.squareColour = "Black"
#     print(newPawn.squareColour)
#     print(newPiece.squareColour)


# if __name__ == "__main__":
#     main()
