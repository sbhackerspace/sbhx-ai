from board import *
import random
import copy


class MinimaxAI:

	def __init__(self, depth):
		self.depth = depth

	def SetPlayerNumber(self, player):
		self.player = player

	def GetMove(self, board):

		alpha = -1
		beta  = 1

		available_moves = board.GetAvailableMoves()
		
		new_player = self.player + 1
		if new_player > 2:
			new_player = 1

		moves_and_values = []
		for i in range(len(available_moves)):
			moves_and_values.append([available_moves[i],alpha])

		random.shuffle(moves_and_values)

		for i in range(len(moves_and_values)):
			move = moves_and_values[i][0]
			board.Move(self.player, move)
			value =  (self.GetMoveMinimax(board, new_player, self.depth-1, alpha, beta))
			moves_and_values[i][1] = value
			board.Unmove(move)

			alpha = max(alpha, value)
			
			if value >= beta:
				break # we have a winning solution

		#print("result", moves_and_values)

		for (m,v) in moves_and_values:
			if v == alpha:
				#print("making move", m)
				#print("")
				return m 


		return -1

	def GetMoveMinimax(self, board, player, depth, alpha, beta):

		winner = board.GetWinner()

		if winner != 0:
			if winner == self.player:
				return 1
			else:
				return -1


		if depth <= 0:
			return 0 # our poor estimate

		available_moves = board.GetAvailableMoves()
		
		if available_moves == []:
			return 0

		new_player = player + 1
		if new_player > 2:
			new_player = 1

		if player == self.player: #maximize

			for m in available_moves:
				board.Move(player, m)
				alpha = max(alpha, self.GetMoveMinimax(board, new_player, depth-1, alpha, beta))
				board.Unmove(m)
			
				if beta <= alpha:
					break;

			return alpha 

		else: #minimize

			for m in available_moves:
				board.Move(player, m)
				beta = min(beta, self.GetMoveMinimax(board, new_player, depth-1, alpha, beta))
				board.Unmove(m)
			
				if beta <= alpha:
					break;

			return beta


