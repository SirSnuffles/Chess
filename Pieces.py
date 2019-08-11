class Piece():
	def __init__(self):
		pass

class Rook(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'Rook'

class Knight(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'Knight'

class Bishop(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'Bishop'

class Queen(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'Queen'

class King(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'King'

class Pawn(Piece):
	def __init__(self):
		Piece.__init__(self)
		self.name = 'Pawn'

