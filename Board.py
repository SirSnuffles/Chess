import Pieces



class Board():
	def __init__(self):
		self.BoardArray = [['' for x in range(8)]for y in range(8)]
		wRook1 = Pieces.Rook()
		wRook2 = Pieces.Rook()
		wKnight1 = Pieces.Knight()
		wKnight2 = Pieces.Knight()
		wBishop1 = Pieces.Bishop()
		wBishop2 = Pieces.Bishop()
		wQueen1 = Pieces.Queen()
		wKing1 = Pieces.King()
		wPawn1 = Pieces.Pawn()
		wPawn2 = Pieces.Pawn()
		wPawn3 = Pieces.Pawn()
		wPawn4 = Pieces.Pawn()
		wPawn5 = Pieces.Pawn()
		wPawn6 = Pieces.Pawn()
		wPawn7 = Pieces.Pawn()
		wPawn8 = Pieces.Pawn()

		bRook1 = Pieces.Rook()
		bRook2 = Pieces.Rook()
		bKnight1 = Pieces.Knight()
		bKnight2 = Pieces.Knight()
		bBishop1 = Pieces.Bishop()
		bBishop2 = Pieces.Bishop()
		bQueen1 = Pieces.Queen()
		bKing1 = Pieces.King()
		bPawn1 = Pieces.Pawn()
		bPawn2 = Pieces.Pawn()
		bPawn3 = Pieces.Pawn()
		bPawn4 = Pieces.Pawn()
		bPawn5 = Pieces.Pawn()
		bPawn6 = Pieces.Pawn()
		bPawn7 = Pieces.Pawn()
		bPawn8 = Pieces.Pawn()

		self.BoardArray[0][0] = wRook1.name
		self.BoardArray[7][0] = wRook2.name
		self.BoardArray[1][0] = wKnight1.name
		self.BoardArray[6][0] = wKnight2.name
		self.BoardArray[2][0] = wBishop1.name
		self.BoardArray[5][0] = wBishop2.name
		self.BoardArray[3][0] = wQueen1.name
		self.BoardArray[4][0] = wKing1.name

		self.BoardArray[0][1] = wPawn1.name
		self.BoardArray[1][1] = wPawn2.name
		self.BoardArray[2][1] = wPawn3.name
		self.BoardArray[3][1] = wPawn4.name
		self.BoardArray[4][1] = wPawn5.name
		self.BoardArray[5][1] = wPawn6.name
		self.BoardArray[6][1] = wPawn7.name
		self.BoardArray[7][1] = wPawn8.name

		self.BoardArray[0][7] = bRook1.name
		self.BoardArray[7][7] = bRook2.name
		self.BoardArray[1][7] = bKnight1.name
		self.BoardArray[6][7] = bKnight2.name
		self.BoardArray[2][7] = bBishop1.name
		self.BoardArray[5][7] = bBishop2.name
		self.BoardArray[3][7] = bQueen1.name
		self.BoardArray[4][7] = bKing1.name

		self.BoardArray[0][6] = bPawn1.name
		self.BoardArray[1][6] = bPawn2.name
		self.BoardArray[2][6] = bPawn3.name
		self.BoardArray[3][6] = bPawn4.name
		self.BoardArray[4][6] = bPawn5.name
		self.BoardArray[5][6] = bPawn6.name
		self.BoardArray[6][6] = bPawn7.name
		self.BoardArray[7][6] = bPawn8.name

	def __repr__(self):
		for row in self.BoardArray:
			print(row)

	def move(self, piece, pos):
		

def main():
	newBoard = Board()
	newBoard.__repr__()

if __name__ == '__main__':
	main()		