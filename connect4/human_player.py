from board import *


class Human:

	def __init__(self):
		pass

	def SetPlayerNumber(self, player):
		self.player = player

	def GetMove(self, board):

		board.Display()

		available_moves = board.GetAvailableMoves()

		while True:
			print("Player ", self.player, " (", board.player_chars[self.player], "), please enter a move:", sep='')
			
			move = input()
			try:
				move = int(move)
			except:
				pass

			for m in available_moves:
				if move == m:
					return move

			print("Invalid Move!")

		return -1
	


