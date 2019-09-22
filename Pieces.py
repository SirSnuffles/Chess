


class Square():
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
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        self.possibleMoves = []
        origLocation = self.location
        curLocation = origLocation
        curLocation = (curLocation[0] + 1, curLocation[1])
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print(type(board[curLocation[1]][curLocation[0]]))
                    print('dontpass1')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1])
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1])
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print(type(board[curLocation[1]][curLocation[0]]))
                    print('dontpass2')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1])
        
        curLocation = origLocation
        curLocation = (curLocation[0], curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print(type(board[curLocation[1]][curLocation[0]]))
                    print('dontpass3')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0], curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print(type(board[curLocation[1]][curLocation[0]]))
                    print('dontpass4')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] + 1)
        curLocation = origLocation


class Knight(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Knight"
        self.location = location
        self.colour = colour
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        #need to prevent possiblemoves from being negative values inside this function
        #could use simplification
        self.possibleMoves = []
        toAddPossibleMoves = ()
        toAddPossibleMoves += (((self.location[0] + 2), (self.location[1] - 1)),)
        toAddPossibleMoves += (((self.location[0] - 2), (self.location[1] - 1)),)
        toAddPossibleMoves += (((self.location[0] + 2), (self.location[1] + 1)),)
        toAddPossibleMoves += (((self.location[0] - 2), (self.location[1] + 1)),)
        toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] - 2)),)
        toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] - 2)),)
        toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] + 2)),)
        toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] + 2)),)
        #check if in bounds of the board
        for move in toAddPossibleMoves:
            if move[0] in range(8) and move[1] in range(8):
                self.possibleMoves += (move),


class Bishop(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Bishop"
        self.location = location
        self.colour = colour
        self.selected = False
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        # print(self.location, type(self.location), "HERE!")
        self.possibleMoves = []
        origLocation = self.location
        curLocation = origLocation
        # print(gui.GuiBoard.printBoard(self), "Here")
        curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take')
                    curLocation = (curLocation[0] + 1, curLocation[1] + 1)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take')
                    curLocation = (curLocation[0] - 1, curLocation[1] - 1)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take')
                    curLocation = (curLocation[0] + 1, curLocation[1] - 1)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take')
                    curLocation = (curLocation[0] - 1, curLocation[1] + 1)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] + 1)
        origLocation = ()


class Queen(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)

        self.squareColour = squareColour
        self.name = "Queen"
        self.location = location
        self.colour = colour
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):

        self.possibleMoves = []
        origLocation = self.location
        curLocation = origLocation
        curLocation = (curLocation[0] + 1, curLocation[1])
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    # self.possibleMoves += ((curLocation[1], curLocation[0]),)
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1])
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1])
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves = ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1])
        curLocation = origLocation
        curLocation = (curLocation[0], curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0], curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0], curLocation[1] + 1)
        curLocation = origLocation
        curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] + 1)
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + 1, curLocation[1] - 1)
        curLocation = origLocation
        curLocation = (curLocation[0] - 1, curLocation[1] + 1)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    print('allow take', board[curLocation[1]][curLocation[0]], board[curLocation[1]][curLocation[0]].location)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    print('allied piece in way')
                    break

            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] - 1, curLocation[1] + 1)
        print(self.possibleMoves)

class King(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "King"
        self.location = location
        self.colour = colour
        self.possibleMove = False #Also considered, checked!
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        self.possibleMoves = []
        toAddPossibleMoves = ()
        toAddPossibleMoves += (((self.location[0] + 1), (self.location[1])),)
        toAddPossibleMoves += (((self.location[0] - 1), (self.location[1])),)
        toAddPossibleMoves += (((self.location[0]), (self.location[1] + 1)),)
        toAddPossibleMoves += (((self.location[0]), (self.location[1] - 1)),)
        toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] + 1)),)
        toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] + 1)),)
        toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] - 1)),)
        toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] - 1)),)
        #to check if possible move is in bounds of the board
        for move in toAddPossibleMoves:
            if move[0] in range(8) and move[1] in range(8):
                self.possibleMoves += (move),

class Pawn(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Pawn"
        self.location = location
        self.colour = colour
        self.AllowDoubleMove = True
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        self.possibleMoves = []
        toAddPossibleMoves = ()
        if self.colour == "White":
            #if there is not piece in front of pawn
            if not isinstance(board[self.location[1] + 1][self.location[0]], Piece):
                toAddPossibleMoves += (((self.location[0]), (self.location[1] + 1)),)
                if self.AllowDoubleMove == True:
                    self.AllowDoubleMove = False
                    #if not moved before
                    if not isinstance(board[self.location[1] + 2][self.location[0]], Piece):
                        toAddPossibleMoves += (((self.location[0]), (self.location[1] + 2)),)
            #if there is a piece to take(right)
            if isinstance(board[self.location[1] + 1][self.location[0] + 1], Piece):
                toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] + 1)),)
            #if there is a piece to take(left)
            if isinstance(board[self.location[1] + 1][self.location[0] - 1], Piece):
                toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] + 1)),)
        elif self.colour == "Black":
            if not isinstance(board[self.location[1] - 1][self.location[0]], Piece):
                toAddPossibleMoves += (((self.location[0]), (self.location[1] - 1)),)
                if self.AllowDoubleMove == True:
                    self.AllowDoubleMove = False
                    #if not moved before
                    if not isinstance(board[self.location[1] - 2][self.location[0]], Piece):
                        toAddPossibleMoves += (((self.location[0]), (self.location[1] - 2)),)
            #if there is a piece to take(left)
            if isinstance(board[self.location[1] - 1][self.location[0] - 1], Piece):
                toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] - 1)),)
            #if there is a piece to take(right)
            if isinstance(board[self.location[1] - 1][self.location[0] + 1], Piece):
                toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] - 1)),)

        for move in toAddPossibleMoves:
            if move[0] in range(8) and move[1] in range(8):
                self.possibleMoves += (move),

