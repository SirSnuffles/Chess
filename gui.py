from Main import tk, Pieces, Image, ImageTk




class GuiBoard(tk.Frame):
	def __init__(self, parent, board, Player1, Player2, *args, **kwargs):
		"""setup the buttons, cliboard, tkinter frame, and images to be used
		in the game of checkers"""

		self.button = [["" for x in range(8)] for y in range(8)]
		# self.board = Board.Board()
		self.initialButtonPush = ()
		self.buttonPushed = ""
		self.nextButton = ()

		# setup tkinter frame
		tk.Frame.__init__(self, parent, *args, **kwargs)
		parent = parent
		# call setup functions
		self.setupButtonImages()
		self.setupBoard()
		self.NewBoard = board
		self.Player1 = Player1
		self.Player2 = Player2
		
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








		BlackSquare = Image.open("Icons/BlackSquare.png")
		self.BlackSquareImage = ImageTk.PhotoImage(BlackSquare)

		WhiteSquare = Image.open("Icons/WhiteSquare.png")
		self.WhiteSquareImage = ImageTk.PhotoImage(WhiteSquare)

		BlackSquarePos = Image.open("Icons/BlackSquarePos.png")
		self.BlackSquarePosImage = ImageTk.PhotoImage(BlackSquarePos)

		WhiteSquarePos = Image.open("Icons/WhiteSquarePos.png")
		self.WhiteSquarePosImage = ImageTk.PhotoImage(WhiteSquarePos)

		BlackPawnRedSquare = Image.open("Icons/BlackPawnRedSquare.png")
		self.BlackPawnRedSquareImage = ImageTk.PhotoImage(BlackPawnRedSquare)

		WhitePawnRedSquare = Image.open("Icons/WhitePawnRedSquare.png")
		self.WhitePawnRedSquareImage = ImageTk.PhotoImage(WhitePawnRedSquare)

		BlackRookRedSquare = Image.open("Icons/BlackRookRedSquare.png")
		self.BlackRookRedSquareImage = ImageTk.PhotoImage(BlackRookRedSquare)

		WhiteRookRedSquare = Image.open("Icons/WhiteRookRedSquare.png")
		self.WhiteRookRedSquareImage = ImageTk.PhotoImage(WhiteRookRedSquare)

		BlackKnightRedSquare = Image.open("Icons/BlackKnightRedSquare.png")
		self.BlackKnightRedSquareImage = ImageTk.PhotoImage(BlackKnightRedSquare)

		WhiteKnightRedSquare = Image.open("Icons/WhiteKnightRedSquare.png")
		self.WhiteKnightRedSquareImage = ImageTk.PhotoImage(WhiteKnightRedSquare)

		BlackBishopRedSquare = Image.open("Icons/BlackBishopRedSquare.png")
		self.BlackBishopRedSquareImage = ImageTk.PhotoImage(BlackBishopRedSquare)

		WhiteBishopRedSquare = Image.open("Icons/WhiteBishopRedSquare.png")
		self.WhiteBishopRedSquareImage = ImageTk.PhotoImage(WhiteBishopRedSquare)

		BlackKingRedSquare = Image.open("Icons/BlackKingRedSquare.png")
		self.BlackKingRedSquareImage = ImageTk.PhotoImage(BlackKingRedSquare)

		WhiteKingRedSquare = Image.open("Icons/WhiteKingRedSquare.png")
		self.WhiteKingRedSquareImage = ImageTk.PhotoImage(WhiteKingRedSquare)

		BlackQueenRedSquare = Image.open("Icons/BlackQueenRedSquare.png")
		self.BlackQueenRedSquareImage = ImageTk.PhotoImage(BlackQueenRedSquare)

		WhiteQueenRedSquare = Image.open("Icons/WhiteQueenRedSquare.png")
		self.WhiteQueenRedSquareImage = ImageTk.PhotoImage(WhiteQueenRedSquare)

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

	def loadPossibleMoves(self, x, y):
		if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Piece):
			self.NewBoard.BoardArray[x][y].genPossibleMove(self.NewBoard.BoardArray)
		else:
			return
		for posLocation in self.NewBoard.BoardArray[x][y].possibleMoves:
			if isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Square):
				if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove == True:
					self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove = False
					if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.BlackSquareImage
					)
					elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.WhiteSquareImage
					)
				elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove == False:
					self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove = True
					if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "Black":
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.BlackSquarePosImage
					)
					elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].squareColour == "White":
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.WhiteSquarePosImage
					)
			elif isinstance(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]], Pieces.Piece):
				if self.NewBoard.BoardArray[posLocation[1]][posLocation[0]].colour != self.NewBoard.BoardArray[x][y].colour:

					if self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove == True:
						self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove = False
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.returnPossibleTakeMove(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]])
						)
					elif self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove == False:
						self.NewBoard.BoardArray[posLocation[0]][posLocation[1]].possibleMove = True
						self.button[posLocation[1]][posLocation[0]].config(
						image=self.returnPossibleTakeMove(self.NewBoard.BoardArray[posLocation[1]][posLocation[0]])
						)

	def returnPossibleTakeMove(self, piece):
		# configure images based on squarecolour and piece type and piece colour
		if piece.name == "Pawn" and piece.colour == "White":
			return self.WhitePawnRedSquareImage
		elif piece.name == "Pawn" and piece.colour == "Black":
			return self.BlackPawnRedSquareImage
		elif piece.name == "Rook" and piece.colour == "White":
			return self.WhiteRookRedSquareImage
		elif piece.name == "Rook" and piece.colour == "Black":
			return self.BlackRookRedSquareImage
		elif piece.name == "Knight" and piece.colour == "White":
			return self.WhiteKnightRedSquareImage
		elif piece.name == "Knight" and piece.colour == "Black":
			return self.BlackKnightRedSquareImage
		elif piece.name == "Bishop" and piece.colour == "White":
			return self.WhiteBishopRedSquareImage
		elif piece.name == "Bishop" and piece.colour == "Black":
			return self.BlackBishopRedSquareImage
		elif piece.name == "Queen" and piece.colour == "White":
			return self.WhiteQueenRedSquareImage
		elif piece.name == "Queen" and piece.colour == "Black":
			return self.BlackQueenRedSquareImage
		elif piece.name == "King" and piece.colour == "White":
			return self.WhiteKingRedSquareImage
		elif piece.name == "King" and piece.colour == "Black":
			return self.BlackKingRedSquareImage

	def recordInput(self, x, y):
		moveMade = False
		if not moveMade:

			if self.initialButtonPush == ():  # initial button push
				self.initialButtonPush = (x, y)
				self.button[x][y].config(
						image=self.returnPossibleTakeMove(self.NewBoard.BoardArray[x][y])
						)
				# print(self.NewBoard.BoardArray[x][y], type(self.NewBoard.BoardArray[x][y]))
				if isinstance(self.NewBoard.BoardArray[x][y], Pieces.Piece):

					if self.NewBoard.BoardArray[x][y].colour == 'White' and self.Player1.turn:
						#player1 turn
						self.loadPossibleMoves(x,y)

					elif self.NewBoard.BoardArray[x][y].colour == "Black" and self.Player2.turn:
						#player2 turn
						self.loadPossibleMoves(x,y)
				else:
					self.initialButtonPush = ()

			elif self.nextButton != self.initialButtonPush and self.NewBoard.BoardArray[y][x].possibleMove:
				# #allow move
				self.loadPossibleMoves(self.initialButtonPush[0],self.initialButtonPush[1])
				self.nextButton = (x, y)

				self.move(self.initialButtonPush, self.nextButton)
				if self.Player1.turn == True:
					self.Player1.turn = False
					self.Player2.turn = True
				elif self.Player2.turn == True:
					self.Player1.turn = True
					self.Player2.turn = False
				self.initialButtonPush = ()
				self.updateBoard()

			elif self.nextButton != self.initialButtonPush and not self.NewBoard.BoardArray[y][x].possibleMove:
				self.loadPossibleMoves(self.initialButtonPush[0], self.initialButtonPush[1])
				self.nextButton = ()
				self.initialButtonPush = ()

				self.updateBoard()

			elif self.initialButtonPush == (x, y):
				#deselect initialButtonPush and toggle possibleMoves
				self.loadPossibleMoves(x,y)
				self.initialButtonPush = ()
				self.updateBoard()

				
	def move(self, pieceLoc, posLoc):
		posColour = self.NewBoard.BoardArray[posLoc[0]][posLoc[1]].squareColour #white

		print(self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]])
		#for castling@@@@@@@@@@@@@@@@@@@@
		self.castle(pieceLoc, posLoc)

		self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].isMoved = True
		self.NewBoard.BoardArray[posLoc[0]][posLoc[1]], \
		self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].location, \
		self.NewBoard.BoardArray[posLoc[0]][posLoc[1]].squareColour, \
		self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]] = \
		self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]], \
		(posLoc[1], posLoc[0]), \
		posColour, \
		Pieces.Square(self.NewBoard.BoardArray[pieceLoc[1]][pieceLoc[0]].squareColour)

		self.updateBoard()

	def castle(self, pieceLoc, posLoc):
		"""Logic for castling"""
		#Should be abstracted away from gui file
		if isinstance(self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]], Pieces.King):
			if not self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled:
				print(posLoc)
				print(type(posLoc))
				
				if self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].colour == "White" and not self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled:
					if posLoc == (0, 6):
						self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled = True
						self.NewBoard.BoardArray[0][7], \
						self.NewBoard.BoardArray[0][5] = \
						Pieces.Square("White"), \
						self.NewBoard.BoardArray[0][7]
					if posLoc == (0, 2):
						self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled = True
						self.NewBoard.BoardArray[0][0], \
						self.NewBoard.BoardArray[0][3] = \
						Pieces.Square("Black"), \
						self.NewBoard.BoardArray[0][0]

						self.NewBoard.BoardArray[0][3].squareColour = "White"
				if self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].colour == "Black" and not self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled:
					if posLoc == (7, 6):
						self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled = True
						self.NewBoard.BoardArray[7][7], \
						self.NewBoard.BoardArray[7][5] = \
						Pieces.Square("Black"), \
						self.NewBoard.BoardArray[7][7]
					if posLoc == (7, 2):
						self.NewBoard.BoardArray[pieceLoc[0]][pieceLoc[1]].castled = True
						self.NewBoard.BoardArray[7][0], \
						self.NewBoard.BoardArray[7][3] = \
						Pieces.Square("White"), \
						self.NewBoard.BoardArray[7][0]

						self.NewBoard.BoardArray[7][3].squareColour = "Black"

	def updateBoard(self):
		# update buttons with images of self.board
		# TODO:
		# collapse to config when self.board is edited
		for indx, x in enumerate(self.NewBoard.BoardArray):
			# print(x.possibleMove)
			for indy, y in enumerate(x):
				y.possibleMove = False
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
				elif isinstance(y, Pieces.Square):
					if y.squareColour == "White":
						self.button[indx][indy].config(
							image=self.WhiteSquareImage
						)
					elif y.squareColour == "Black":
						self.button[indx][indy].config(
							image=self.BlackSquareImage
						)
				




