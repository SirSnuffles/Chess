#import list for all files
import tkinter as tk
from PIL import Image, ImageTk
import Board
import Pieces
import gui
import Player


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
	print(NewBoard)
	gui.GuiBoard(root, NewBoard, Player1, Player2).pack(side="top", fill="both", expand=True)
	root.mainloop()

if __name__ == '__main__':
	main()