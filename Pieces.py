import gui

#TODO:
#must prevent iterable possibleMoves through other pieces
#must check if the possibleMove is an enemy piece and offer to take.



class Square:
    def __init__(self, squareColour):
        self.name = squareColour
        self.squareColour = squareColour
        self.possibleMove = False
        # print(self.squareColour)


class Piece():
    def __init__(self):
        # Square.__init__(self)
        self.name = ""
        self.possibleMoves = []


class Rook(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Rook"
        self.location = location
        self.colour = colour

    def genPossibleMove(self):
        origLocation = self.location
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1])
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1])
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] + 1)


class Knight(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Knight"
        self.location = location
        self.colour = colour

    def genPossibleMove(self):
        #need to prevent possiblemoves from being negative values inside this function
        #could use simplification
        self.possibleMoves += (((self.location[0] + 2), (self.location[1] - 1)),)
        self.possibleMoves += (((self.location[0] - 2), (self.location[1] - 1)),)
        self.possibleMoves += (((self.location[0] + 2), (self.location[1] + 1)),)
        self.possibleMoves += (((self.location[0] - 2), (self.location[1] + 1)),)
        self.possibleMoves += (((self.location[0] + 1), (self.location[1] - 2)),)
        self.possibleMoves += (((self.location[0] - 1), (self.location[1] - 2)),)
        self.possibleMoves += (((self.location[0] + 1), (self.location[1] + 2)),)
        self.possibleMoves += (((self.location[0] - 1), (self.location[1] + 2)),)


class Bishop(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Bishop"
        self.location = location
        self.colour = colour
        self.selected = False

    def genPossibleMove(self):
        # print(self.location, type(self.location), "HERE!")
        origLocation = self.location
        curLocation = origLocation
        # print(gui.GuiBoard.printBoard(self), "Here")
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            # if 
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] + 1)
        # origLocation = ()


class Queen(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Queen"
        self.location = location
        self.colour = colour

    def genPossibleMove(self):
        origLocation = self.location
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1])
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1])
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] + 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        curLocation = origLocation
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] + 1)


class King(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "King"
        self.location = location
        self.colour = colour
        self.isChecked = False

    def genPossibleMove(self):
        self.possibleMoves += (((self.location[0] + 1), (self.location[1])),)
        self.possibleMoves += (((self.location[0] - 1), (self.location[1])),)
        self.possibleMoves += (((self.location[0]), (self.location[1] + 1)),)
        self.possibleMoves += (((self.location[0]), (self.location[1] - 1)),)
        self.possibleMoves += (((self.location[0] + 1), (self.location[1] + 1)),)
        self.possibleMoves += (((self.location[0] - 1), (self.location[1] + 1)),)
        self.possibleMoves += (((self.location[0] + 1), (self.location[1] - 1)),)
        self.possibleMoves += (((self.location[0] - 1), (self.location[1] - 1)),)


class Pawn(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Pawn"
        self.location = location
        self.colour = colour
        self.AllowDoubleMove = True

    def genPossibleMove(self):
        if self.colour == "White":
            self.possibleMoves += (((self.location[0]), (self.location[1] + 1)),)
            if self.AllowDoubleMove == True:
                self.possibleMoves += (((self.location[0]), (self.location[1] + 2)),)

        elif self.colour == "Black":
            self.possibleMoves += (((self.location[0]), (self.location[1] - 1)),)
            if self.AllowDoubleMove == True:
                self.possibleMoves += (((self.location[0]), (self.location[1] - 2)),)
