import tkinter as tk
from PIL import Image, ImageTk
import Board
import Pieces as Pieces


class GuiBoard(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """setup the buttons, cliboard, tkinter frame, and images to be used
		in the game of checkers"""

        self.button = [["" for x in range(8)] for y in range(8)]
        self.board = [["" for x in range(8)] for y in range(8)]

        # self.board = Board.Board()
        self.selectedButton = ()
        self.buttonPushed = ""
        self.nextButton = ()

        # setup tkinter frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent = parent
        # call setup functions
        self.setupButtonImages()
        self.setupBoard()

        self.NewBoard = Board.Board()

        self.updateBoard()

    def setupButtonImages(self):
        # Open the images that are saved locally
        BlackSquare = Image.open("Icons/BlackSquare.png")
        self.BlackSquareImage = ImageTk.PhotoImage(BlackSquare)

        WhiteSquare = Image.open("Icons/WhiteSquare.png")
        self.WhiteSquareImage = ImageTk.PhotoImage(WhiteSquare)

        BlackSquarePos = Image.open("Icons/BlackSquarePos.png")
        self.BlackSquarePosImage = ImageTk.PhotoImage(BlackSquarePos)

        WhiteSquarePos = Image.open("Icons/WhiteSquarePos.png")
        self.WhiteSquarePosImage = ImageTk.PhotoImage(WhiteSquarePos)

        BlackPawnBlackSquare = Image.open("Icons/BlackPawnBlackSquare.png")
        self.BlackPawnBlackSquareImage = ImageTk.PhotoImage(BlackPawnBlackSquare)

        BlackPawnWhiteSquare = Image.open("Icons/BlackPawnWhiteSquare.png")
        self.BlackPawnWhiteSquareImage = ImageTk.PhotoImage(BlackPawnWhiteSquare)

        WhitePawnBlackSquare = Image.open("Icons/WhitePawnBlackSquare.png")
        self.WhitePawnBlackSquareImage = ImageTk.PhotoImage(WhitePawnBlackSquare)

        WhitePawnWhiteSquare = Image.open("Icons/WhitePawnWhiteSquare.png")
        self.WhitePawnWhiteSquareImage = ImageTk.PhotoImage(WhitePawnWhiteSquare)

        BlackRookBlackSquare = Image.open("Icons/BlackRookBlackSquare.png")
        self.BlackRookBlackSquareImage = ImageTk.PhotoImage(BlackRookBlackSquare)

        BlackRookWhiteSquare = Image.open("Icons/BlackRookWhiteSquare.png")
        self.BlackRookWhiteSquareImage = ImageTk.PhotoImage(BlackRookWhiteSquare)

        WhiteRookBlackSquare = Image.open("Icons/WhiteRookBlackSquare.png")
        self.WhiteRookBlackSquareImage = ImageTk.PhotoImage(WhiteRookBlackSquare)

        WhiteRookWhiteSquare = Image.open("Icons/WhiteRookWhiteSquare.png")
        self.WhiteRookWhiteSquareImage = ImageTk.PhotoImage(WhiteRookWhiteSquare)

        BlackKnightBlackSquare = Image.open("Icons/BlackKnightBlackSquare.png")
        self.BlackKnightBlackSquareImage = ImageTk.PhotoImage(BlackKnightBlackSquare)

        BlackKnightWhiteSquare = Image.open("Icons/BlackKnightWhiteSquare.png")
        self.BlackKnightWhiteSquareImage = ImageTk.PhotoImage(BlackKnightWhiteSquare)

        WhiteKnightBlackSquare = Image.open("Icons/WhiteKnightBlackSquare.png")
        self.WhiteKnightBlackSquareImage = ImageTk.PhotoImage(WhiteKnightBlackSquare)

        WhiteKnightWhiteSquare = Image.open("Icons/WhiteKnightWhiteSquare.png")
        self.WhiteKnightWhiteSquareImage = ImageTk.PhotoImage(WhiteKnightWhiteSquare)

        BlackBishopBlackSquare = Image.open("Icons/BlackBishopBlackSquare.png")
        self.BlackBishopBlackSquareImage = ImageTk.PhotoImage(BlackBishopBlackSquare)

        BlackBishopWhiteSquare = Image.open("Icons/BlackBishopWhiteSquare.png")
        self.BlackBishopWhiteSquareImage = ImageTk.PhotoImage(BlackBishopWhiteSquare)

        WhiteBishopBlackSquare = Image.open("Icons/WhiteBishopBlackSquare.png")
        self.WhiteBishopBlackSquareImage = ImageTk.PhotoImage(WhiteBishopBlackSquare)

        WhiteBishopWhiteSquare = Image.open("Icons/WhiteBishopWhiteSquare.png")
        self.WhiteBishopWhiteSquareImage = ImageTk.PhotoImage(WhiteBishopWhiteSquare)

        BlackKingBlackSquare = Image.open("Icons/BlackKingBlackSquare.png")
        self.BlackKingBlackSquareImage = ImageTk.PhotoImage(BlackKingBlackSquare)

        BlackKingWhiteSquare = Image.open("Icons/BlackKingWhiteSquare.png")
        self.BlackKingWhiteSquareImage = ImageTk.PhotoImage(BlackKingWhiteSquare)

        WhiteKingBlackSquare = Image.open("Icons/WhiteKingBlackSquare.png")
        self.WhiteKingBlackSquareImage = ImageTk.PhotoImage(WhiteKingBlackSquare)

        WhiteKingWhiteSquare = Image.open("Icons/WhiteKingWhiteSquare.png")
        self.WhiteKingWhiteSquareImage = ImageTk.PhotoImage(WhiteKingWhiteSquare)

        BlackQueenBlackSquare = Image.open("Icons/BlackQueenBlackSquare.png")
        self.BlackQueenBlackSquareImage = ImageTk.PhotoImage(BlackQueenBlackSquare)

        BlackQueenWhiteSquare = Image.open("Icons/BlackQueenWhiteSquare.png")
        self.BlackQueenWhiteSquareImage = ImageTk.PhotoImage(BlackQueenWhiteSquare)

        WhiteQueenBlackSquare = Image.open("Icons/WhiteQueenBlackSquare.png")
        self.WhiteQueenBlackSquareImage = ImageTk.PhotoImage(WhiteQueenBlackSquare)

        WhiteQueenWhiteSquare = Image.open("Icons/WhiteQueenWhiteSquare.png")
        self.WhiteQueenWhiteSquareImage = ImageTk.PhotoImage(WhiteQueenWhiteSquare)

    def setupBoard(self):
        """Sets up the grid of alternating black and white buttons"""
        for x in range(8):
            for y in range(8):
                if x % 2 == 0:
                    if y % 2 == 0:
                        self.button[x][y] = tk.Button(
                            self,
                            image=self.BlackSquareImage,
                            command=lambda x=x, y=y: self.recordInput(x, y),
                        )
                        # self.board[x][y] = Pieces.Piece("b")
                        self.button[x][y].grid(row=x, column=y)
                    elif y % 2 == 1:
                        self.button[x][y] = tk.Button(
                            self,
                            image=self.WhiteSquareImage,
                            command=lambda x=x, y=y: self.recordInput(x, y),
                        )
                        # self.board[x][y] = Pieces.Piece("w")
                        self.button[x][y].grid(row=x, column=y)
                if x % 2 == 1:
                    if y % 2 == 1:
                        self.button[x][y] = tk.Button(
                            self,
                            image=self.BlackSquareImage,
                            command=lambda x=x, y=y: self.recordInput(x, y),
                        )
                        # self.board[x][y] = Pieces.Piece("b")
                        self.button[x][y].grid(row=x, column=y)
                    elif y % 2 == 0:
                        self.button[x][y] = tk.Button(
                            self,
                            image=self.WhiteSquareImage,
                            command=lambda x=x, y=y: self.recordInput(x, y),
                        )
                        # self.board[x][y] = Pieces.Piece("w")
                        self.button[x][y].grid(row=x, column=y)

    def printBoard(self):
        for i in self.NewBoard.BoardArray:
            print(i)

    def setPieceButtonImage(self, x, y):
        """update button images"""
        print(NewBoard.BoardArray[x][y])

    def recordInput(self, x, y):
        print("pushed Location: ", y, x)

        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Pawn):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].squareColour,
            )
            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
            	print(posLocation[0], posLocation[1])
            	print(self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour)
            	if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
            		self.button[posLocation[1]][posLocation[0]].config(
                    image=self.BlackSquarePosImage
                )
            	elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                	self.button[posLocation[1]][posLocation[0]].config(
                    image=self.WhiteSquarePosImage
                )

        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Rook):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].possibleMoves,
            )

            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
                if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
                    print(posLocation[0], posLocation[1])
                    print(self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour)
                    if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.BlackSquarePosImage
                    )
                    elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.WhiteSquarePosImage
                    )


        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Knight):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].possibleMoves,
            )
            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
                if posLocation[0] in range(8) and posLocation[1] in range(8):
                    # if self.NewBoard.BoardArrayposLocation[0],
                    if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
                        # if self.NewBoard.BoardArray[posLocation[1]][posLocation[0]].colour == self.NewBoard.BoardArray[x][y].colour:
                        if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
                            self.button[posLocation[1]][posLocation[0]].config(
                            image=self.BlackSquarePosImage
                        )
                        elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                            self.button[posLocation[1]][posLocation[0]].config(
                            image=self.WhiteSquarePosImage
                        )

        # if button pushes a bishop instance
        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Bishop):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].possibleMoves,
            )

            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
                if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
                    print(posLocation[0], posLocation[1])
                    print(self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour)
                    if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.BlackSquarePosImage
                    )
                    elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.WhiteSquarePosImage
                    )

        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.King):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].possibleMoves,
            )
            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
                if posLocation[0] in range(8) and posLocation[1] in range(8):
                    if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
                        print(posLocation[0], posLocation[1])
                        print(self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour)
                        if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
                            self.button[posLocation[1]][posLocation[0]].config(
                            image=self.BlackSquarePosImage
                        )
                        elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                            self.button[posLocation[1]][posLocation[0]].config(
                            image=self.WhiteSquarePosImage
                        )

        if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Queen):
            self.NewBoard.BoardArray[x][y].genPossibleMove()
            print(
                self.NewBoard.BoardArray[x][y],
                self.NewBoard.BoardArray[x][y].possibleMoves,
            )
            for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
                if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
                    print(posLocation[0], posLocation[1])
                    print(self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour)
                    if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.BlackSquarePosImage
                    )
                    elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
                        self.button[posLocation[1]][posLocation[0]].config(
                        image=self.WhiteSquarePosImage
                    )

    def updateBoard(self):
        # update buttons with images of self.board
        # TODO:
        # collapse to config when self.board is edited
        for indx, x in enumerate(self.NewBoard.BoardArray):
            for indy, y in enumerate(x):
                # configure images based on squarecolour and piece type and piece colour
                if y.name == "Pawn" and y.colour == "White":
                    # WhitePawn
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhitePawnWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhitePawnBlackSquareImage
                        )
                elif y.name == "Pawn" and y.colour == "Black":
                    # BlackPawn
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackPawnWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackPawnBlackSquareImage
                        )
                elif y.name == "Rook" and y.colour == "White":
                    # WhiteRook
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhiteRookWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhiteRookBlackSquareImage
                        )
                elif y.name == "Rook" and y.colour == "Black":
                    # BlackRook
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackRookWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackRookBlackSquareImage
                        )
                elif y.name == "Knight" and y.colour == "White":
                    # WhiteKnight
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhiteKnightWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhiteKnightBlackSquareImage
                        )
                elif y.name == "Knight" and y.colour == "Black":
                    # BlackKnight
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackKnightWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackKnightBlackSquareImage
                        )
                elif y.name == "Bishop" and y.colour == "White":
                    # WhiteBishop
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhiteBishopWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhiteBishopBlackSquareImage
                        )
                elif y.name == "Bishop" and y.colour == "Black":
                    # BlackBishop
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackBishopWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackBishopBlackSquareImage
                        )
                elif y.name == "King" and y.colour == "White":
                    # WhiteKing
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhiteKingWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhiteKingBlackSquareImage
                        )
                elif y.name == "King" and y.colour == "Black":
                    # BlackKing
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackKingWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackKingBlackSquareImage
                        )
                elif y.name == "Queen" and y.colour == "White":
                    # WhiteQueen
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.WhiteQueenWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.WhiteQueenBlackSquareImage
                        )
                elif y.name == "Queen" and y.colour == "Black":
                    # BlackQueen
                    if y.squareColour == "White":
                        self.button[indx][indy].config(
                            image=self.BlackQueenWhiteSquareImage
                        )
                    elif y.squareColour == "Black":
                        self.button[indx][indy].config(
                            image=self.BlackQueenBlackSquareImage
                        )


#TODO:
#additional TODO in Pieces.py

#Allow movement of pieces to possible move squares

#prevent possibleMoves going through objects in the board #Could be a problem with the instance
#Board being initiated in the gui class

#tidyup each isinstance(square) and in range(8) for both x and y locations, could be 
#abstracted into a function to keep it simplier



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("530x530")
    root.title("Chess")
    GuiBoard(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
