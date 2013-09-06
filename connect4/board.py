# Board Class

from math import floor

# Board is 7 wide and 6 deep.


class Board:

	def __init__(self, rows=6, cols=7):

		self.rows = rows
		self.cols = cols
		self.board = []
		self.player_chars = ['_','X','O']

		for r in range(rows):
			self.board.append([])
			for c in range(cols):
				self.board[-1].append(0)
	
	def Display(self):

		# Print header
		for c in range(2*self.cols + 1):
			if ((c%2) == 1):
				print(floor(c/2), end='')
			else:
				print(" ", end='')

		print("")

		for c in range(2*self.cols + 1):
			if ((c%2) == 1):
				print("|", end='')
			else:
				print(" ", end='')

		print("")

		for c in range(2*self.cols + 1):
			if ((c%2) == 1):
				print("V", end='')
			else:
				print(" ", end='')

		print("")

		# Print Board 
		for r in range(self.rows):
			print("|", end='')
			for c in range(self.cols):
				if (self.board[r][c] == 1):
					print(self.player_chars[1], end='')
				elif (self.board[r][c] == 2):
					print(self.player_chars[2], end='')
				else:
					print(self.player_chars[0], end='')

				print("|", end='')

			print("")


	def Move(self, player, col):

		if col < 0 or col >= self.cols:
			return False

		row = -1
		for r in range(self.rows - 1, -1, -1): # walk column from bottom to top	
			if (self.board[r][col] == 0):
				row = r
				break

		if (row == -1):
			return False

		self.board[row][col] = player
		return True

	def Unmove(self, col):

		if col < 0 or col >= self.cols:
			return False

		for r in range(self.rows): # walk column from top to bottom
			if (self.board[r][col] != 0):
				self.board[r][col] = 0
				break
		
		return True

	def GetAvailableMoves(self):
		moves = []
		for c in range(self.cols):
			if self.board[0][c] == 0:
				moves.append(c)
		return moves

	def GetWinner(self):

		connect = 4;

		# check verticle
		for c in range(self.cols):
			last_player = 0
			streak = 0
			for r in range(self.rows - 1, -1, -1):
				cur_player = self.board[r][c]
				if cur_player == 0:
					break
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player
				
		# check horizontal
		for r in range(self.rows):
			last_player = 0
			streak = 0
			for c in range(self.cols):
				cur_player = self.board[r][c]
				if cur_player == 0:
					last_player = cur_player
					streak = 0	
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player

		# check diagnol \ 
		# above and main diagnol
		for c in range(self.cols):
			last_player = 0
			streak = 0
			diag_len = min(self.rows, self.cols - c)
			if diag_len < connect:
				break
			for d in range(diag_len):
				cur_player = self.board[d][c+d]
				if cur_player == 0:
					last_player = cur_player
					streak = 0	
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player

		# below the main diagnol
		for r in range(1, self.rows):
			last_player = 0
			streak = 0
			diag_len = min(self.rows - r, self.cols)
			if diag_len < connect:
				break
			for d in range(diag_len):
				cur_player = self.board[r+d][d]
				if cur_player == 0:
					last_player = cur_player
					streak = 0	
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player

		# check diagnol / 
		# below and main diagnol
		for c in range(self.cols):
			last_player = 0
			streak = 0
			diag_len = min(self.rows, self.cols - c)
			if diag_len < connect:
				break
			for d in range(diag_len):
				cur_player = self.board[(self.rows-1)-d][c+d]
				if cur_player == 0:
					last_player = cur_player
					streak = 0	
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player

		# above the main diagnol
		for r in range(1, self.rows):
			last_player = 0
			streak = 0
			diag_len = min(self.rows - r, self.cols)
			if diag_len < connect:
				break
			for d in range(diag_len):
				cur_player = self.board[((self.rows-1)-r)-d][d]
				if cur_player == 0:
					last_player = cur_player
					streak = 0	
				elif cur_player != last_player:
					last_player = cur_player
					streak = 1	
				else:
					streak += 1
					if streak >= connect:
						return cur_player

		return 0


	def PrintToCSV(self, file_id):

		for r in range(self.rows):
			for c in range(self.cols):
				if (self.board[r][c] == 1):
					file_id.write("1, ")
				elif (self.board[r][c] == 2):
					file_id.write("-1, ")
				else:
					file_id.write("0, ")

if __name__ == "__main__": # simple demo

	b = Board(6,7)

	b.Move(1, 2)
	b.Move(2, 2)
	b.Move(1, 0)
	b.Move(2, 1)

	b.GetWinner()

	b.Display()
