from board import *
import random



class RandomAI:

	def __init__(self):
		pass

	def SetPlayerNumber(self, player):
		self.player = player

	def GetMove(self, board):

		available_moves = board.GetAvailableMoves()
		move = random.sample(available_moves,1)[0]	
		
		return move 
