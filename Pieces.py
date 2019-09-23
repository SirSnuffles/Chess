class Square():
    def __init__(self, squareColour):
        self.name = squareColour
        self.squareColour = squareColour
        self.possibleMove = False
        # print(self.squareColour)


class Piece():
    def __init__(self):
        """parent Piece class containing move information"""
        self.name = ""
        self.possibleMoves = []
        self.isMoved = False

    def generateDiagonal(self, direction, board):
        if direction == "NE":
            x, y = -1, 1
        elif direction == "SE":
            x, y = 1, 1
        elif direction == "SW":
            x, y = 1, -1
        elif direction == "NW":
            x, y = -1, -1
        origLocation = self.location
        curLocation = origLocation
        curLocation = (curLocation[0] + x, curLocation[1] + y)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    curLocation = (curLocation[0] + x, curLocation[1] + y)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + x, curLocation[1] + y)
        origLocation = ()

    def generateHorver(self, direction, board):
        """added horiztonal and vertical possible moves to piece"""
        if direction == "N":
            x, y = 0, -1
        elif direction == "E":
            x, y = 1, 0
        elif direction == "S":
            x, y = 0, 1
        elif direction == "W":
            x, y = -1, 0
        origLocation = self.location
        curLocation = origLocation
        curLocation = (curLocation[0] + x, curLocation[1] + y)
        while curLocation[0] in range(8) and curLocation[1] in range(8):
            if isinstance(board[curLocation[1]][curLocation[0]], Piece):
                if board[curLocation[1]][curLocation[0]].colour == self.oppositeColour:
                    self.possibleMoves += ((curLocation[0], curLocation[1]),)
                    curLocation = (curLocation[0] + x, curLocation[1] + y)
                    break
                if board[curLocation[1]][curLocation[0]].colour == self.colour:
                    break
            self.possibleMoves += ((curLocation[0], curLocation[1]),)
            curLocation = (curLocation[0] + x, curLocation[1] + y)
        origLocation = ()


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
        """Generate possible horiztonal and vertical moves using parent class piece; generateHorver function"""
        self.generateHorver('N', board)
        self.generateHorver('E', board)
        self.generateHorver('S', board)
        self.generateHorver('W', board)


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
        """Generate parent classes diagonal piece moves (northwest, northeast etc"""
        self.generateDiagonal('NW', board)
        self.generateDiagonal('NE', board)
        self.generateDiagonal('SW', board)
        self.generateDiagonal('SE', board)
        

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
        """generate queen moves from parent class functions generateHorver and generateDiagonal"""
        self.generateHorver('N', board)
        self.generateHorver('E', board)
        self.generateHorver('S', board)
        self.generateHorver('W', board)
        self.generateDiagonal('NW', board)
        self.generateDiagonal('NE', board)
        self.generateDiagonal('SW', board)
        self.generateDiagonal('SE', board)
        

class King(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "King"
        self.location = location
        self.colour = colour
        self.castled = False
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
        if self.colour == "White" and self.isMoved == False:
            if isinstance(board[0][7], Rook) and board[0][7].isMoved == False:
                if not isinstance(board[0][5], Piece) and  \
                    not isinstance(board[0][6], Piece):
                    toAddPossibleMoves += ((6, 0),)
            if isinstance(board[0][0], Rook) and board[0][0].isMoved == False:
                if not isinstance(board[0][1], Piece) and \
                    not isinstance(board[0][2], Piece) and \
                    not isinstance(board[0][3], Piece):
                    toAddPossibleMoves += ((2, 0),)
        elif self.colour == "Black" and self.isMoved == False:
            if isinstance(board[7][7], Rook) and board[7][7].isMoved == False:
                if not isinstance(board[7][1], Piece) and \
                    not isinstance(board[7][2], Piece) and \
                    not isinstance(board[7][3], Piece):
                    toAddPossibleMoves += ((2, 7),)
            if isinstance(board[7][0], Rook) and board[7][0].isMoved == False:
                if not isinstance(board[7][5], Piece) and  \
                    not isinstance(board[7][6], Piece):
                    toAddPossibleMoves += ((6, 7),)

        for move in toAddPossibleMoves:
            if move[0] in range(8) and move[1] in range(8):
                self.possibleMoves += ((move),)

        #for castling

        #for white kings


class Pawn(Piece):
    def __init__(self, location, colour, squareColour):
        Piece.__init__(self)
        self.squareColour = squareColour
        self.name = "Pawn"
        self.location = location
        self.colour = colour
        # self.isMoved = True
        self.possibleMove = False
        self.oppositeColour = 'Black' if colour == 'White' else 'White'

    def genPossibleMove(self, board):
        self.possibleMoves = []
        toAddPossibleMoves = ()
        if self.colour == "White":
            #if there is not piece in front of pawn
            if not isinstance(board[self.location[1] + 1][self.location[0]], Piece):
                toAddPossibleMoves += (((self.location[0]), (self.location[1] + 1)),)
                if self.isMoved == False:
                    # self.isMoved = True
                    #if not moved before
                    if not isinstance(board[self.location[1] + 2][self.location[0]], Piece):
                        toAddPossibleMoves += (((self.location[0]), (self.location[1] + 2)),)
            try:
                #if there is a piece to take(right)
                if isinstance(board[self.location[1] + 1][self.location[0] + 1], Piece):
                    toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] + 1)),)
            except IndexError:
                pass
                # print('checking outside of board parameters!')
            try:
                #if there is a piece to take(left)
                if isinstance(board[self.location[1] + 1][self.location[0] - 1], Piece):
                    toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] + 1)),)
            except IndexError:
                pass
                # print('checking outside of board parameters!')

        elif self.colour == "Black":
            if not isinstance(board[self.location[1] - 1][self.location[0]], Piece):
                toAddPossibleMoves += (((self.location[0]), (self.location[1] - 1)),)
                if self.isMoved == False:
                    # self.isMoved = True
                    #if not moved before
                    if not isinstance(board[self.location[1] - 2][self.location[0]], Piece):
                        toAddPossibleMoves += (((self.location[0]), (self.location[1] - 2)),)
            try:
                #if there is a piece to take(left)
                if isinstance(board[self.location[1] - 1][self.location[0] - 1], Piece):
                    toAddPossibleMoves += (((self.location[0] - 1), (self.location[1] - 1)),)
            except IndexError:
                pass
                # print('checking outside of board parameters')
            try:
                #if there is a piece to take(right)
                if isinstance(board[self.location[1] - 1][self.location[0] + 1], Piece):
                    toAddPossibleMoves += (((self.location[0] + 1), (self.location[1] - 1)),)
            except IndexError:
                pass
                # print('checking ouside of board parameters')

        #en passant:



        for move in toAddPossibleMoves:
            if move[0] in range(8) and move[1] in range(8):
                self.possibleMoves += ((move),)