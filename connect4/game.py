import random

from board import *

from human_player import *
from random_ai import *
from minimax_ai import *
from minimax_with_NN_ai import *

class Game:

	def __init__(self, player1, player2, starting_player = 0):

		self.players = [player1, player2]

		self.players[0].SetPlayerNumber(1)
		self.players[1].SetPlayerNumber(2)

		self.board = Board()
		self.winner = 0

		if (starting_player == 0):
			self.current_player = random.sample([1,2],1)[0]
		else:
			self.current_player = starting_player

		self.starting_player = self.current_player

	def Play(self):

		while(self.winner == 0):

			if self.board.GetAvailableMoves() == []:
				break

			temp_board = copy.deepcopy(self.board) # don't let the players modify the board

			move = self.players[self.current_player-1].GetMove(temp_board)

			if(not self.board.Move(self.current_player, move)):
				print("Invalid Move! (", move,").", sep='')
				print("Player ", self.current_player, "loses!", sep='')
				self.current_player += 1
				if self.current_player > 2:
					self.current_player = 1
				self.winner = self.current_player
				break

			self.current_player += 1
			if self.current_player > 2:
				self.current_player = 1
			
			self.winner = self.board.GetWinner()

		return self.winner

	def PrintToCSV(self, file_id):

		self.board.PrintToCSV(file_id)

		if (self.winner == 1):
			file_id.write("1\n")
		elif (self.winner == 2):
			file_id.write("-1\n")
		else:
			file_id.write("0\n")


if __name__ == "__main__": # simple demo

	# Choose the players

	p1 = Human()
	#p2 = MinimaxAI(4)
	p2 = MinimaxNNAI(4)
	#p1 = Human()
	#p1 = RandomAI()
	#p2 = RandomAI()
	#p2 = Human(2)

	g = Game(p1, p2)
	winner = g.Play()

	#g.PrintToCSV()
	g.board.Display()

	print("Player", winner, "wins!!")


