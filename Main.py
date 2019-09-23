#import list for all files
import tkinter as tk
from PIL import Image, ImageTk
import Board
import Pieces
import gui
import Player


#TODO:
#Main.py@@@@@@@@@@@@@
#convert to .exe using cxfreeze
#Dont allow other moves if king in check
#Maybe allow multiplayer through sockets??
# 
#TODO:
#gui.py@@@@@@@@@@@@@@

#

# TODO:
 #Pieces.py@@@@@@@@@@@@@
# Implement en passant (spelling????) bloody french :D
# Castling could use abstraction
# Need to only allow the king to move if is in check
#detecting checkmate
#minimax solution (somehow...)

def main():
# name, turn, colour, winStatus,timeRemaining,numberOfPieces
	time = 600
	piecePoints = 39
	Player1 = Player.Player('Alex', True, 'White', False, time, piecePoints)
	Player2 = Player.Player('Bob', False, 'Black', False, time, piecePoints)

	root = tk.Tk()
	root.geometry("530x530")
	root.title("Chess")
	NewBoard = Board.MainBoard()

	gui.GuiBoard(root, NewBoard, Player1, Player2).pack(side="top", fill="both", expand=True)
	root.mainloop()

if __name__ == '__main__':
	main()