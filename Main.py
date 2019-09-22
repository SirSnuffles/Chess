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

#TODO:
#gui.py@@@@@@@@@@@@@@

#

#tidyup each isinstance(square) and in range(8) for both x and y locations, could be 
#abstracted into a function to keep it simplier

#implement a turn based system only allowing alternate players selecting their own coloured pieces
#

# TODO:
 #Pieces.py@@@@@@@@@@@@@
# Implement en passant (spelling????) bloody french :D
# Implement castling
#

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