import random

class LCycleAIStraight:

    def __init__(self, myCycle, theirCycle, boardX, boardY):
        self._myCycle = myCycle
        self._theirCycle = theirCycle
        self._boardX = boardX
        self._boardY = boardY

    def getMove(self):
        return 'Straight'
        

class LCycleAIAvoidWalls:

	def __init__(self, myCycle, theirCycle, boardX, boardY):
		self._myCycle = myCycle
		self._theirCycle = theirCycle
		self._boardX = boardX
		self._boardY = boardY

	def getMove(self):
		
		if not self._badCell(self._getCellIfMove('Straight')):
			return 'Straight'
		elif not self._badCell(self._getCellIfMove('Left')):
			return 'Left'
		elif not self._badCell(self._getCellIfMove('Right')):
			return 'Right'
		return 'Straight'

	def _getCellIfMove(self, move):
		x,y = self._myCycle.getLoc()
		dir = self._myCycle.getDir()
		
		if move == 'Straight':
			x,y = self._updateXY(x,y,dir)
			
		elif move == 'Left':
			if dir == 'N':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'N')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'S')
			else:
				raise Exception('bad direction')
				
		elif move == 'Right':
			if dir == 'N':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'S')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'N')
			else:
				raise Exception('bad direction')
		else:
				raise Exception('bad move')
				
		return [x,y]

	def _updateXY(self, X,Y,dir):
		x,y = X,Y
		if dir == 'N':
			y -= 1
		elif dir == 'E':
			x += 1
		elif dir == 'S':
			y += 1
		elif dir == 'W':
			x -= 1
		else:
			raise Exception('bad direction')
		return [x,y]

	def _cellOutOfBounds(self, cell):
		x,y = cell
		if x < 0 or y < 0:
			return True
		elif x >= self._boardX or y >= self._boardY:
			return True
		return False

	def _cellCollidesWithTrail(self, cell):
		myTrail = self._myCycle.getTrail()
		theirTrail = self._theirCycle.getTrail()
		for t in myTrail:
			if cell == t:
				return True
		for t in theirTrail:
			if cell == t:
				return True
		return False
		
	def _cellCollidesWithCycle(self, cell):
		if cell == self._theirCycle.getLoc():
			return True
		else:
			return False

	def _badCell(self,cell):
		if self._cellOutOfBounds(cell):
			return True
		if self._cellCollidesWithTrail(cell):
			return True
		if self._cellCollidesWithCycle(cell):
			return True
		return False

class LCycleAIHugRight:

	def __init__(self, myCycle, theirCycle, boardX, boardY):
		self._myCycle = myCycle
		self._theirCycle = theirCycle
		self._boardX = boardX
		self._boardY = boardY

	def getMove(self):
		
		if not self._badCell(self._getCellIfMove('Right')):
			return 'Right'
		elif not self._badCell(self._getCellIfMove('Straight')):
			return 'Straight'
		elif not self._badCell(self._getCellIfMove('Left')):
			return 'Left'
		return 'Straight'

	def _getCellIfMove(self, move):
		x,y = self._myCycle.getLoc()
		dir = self._myCycle.getDir()
		
		if move == 'Straight':
			x,y = self._updateXY(x,y,dir)
			
		elif move == 'Left':
			if dir == 'N':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'N')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'S')
			else:
				raise Exception('bad direction')
				
		elif move == 'Right':
			if dir == 'N':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'S')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'N')
			else:
				raise Exception('bad direction')
		else:
				raise Exception('bad move')
				
		return [x,y]

	def _updateXY(self, X,Y,dir):
		x,y = X,Y
		if dir == 'N':
			y -= 1
		elif dir == 'E':
			x += 1
		elif dir == 'S':
			y += 1
		elif dir == 'W':
			x -= 1
		else:
			raise Exception('bad direction')
		return [x,y]

	def _cellOutOfBounds(self, cell):
		x,y = cell
		if x < 0 or y < 0:
			return True
		elif x >= self._boardX or y >= self._boardY:
			return True
		return False

	def _cellCollidesWithTrail(self, cell):
		myTrail = self._myCycle.getTrail()
		theirTrail = self._theirCycle.getTrail()
		for t in myTrail:
			if cell == t:
				return True
		for t in theirTrail:
			if cell == t:
				return True
		return False
		
	def _cellCollidesWithCycle(self, cell):
		if cell == self._theirCycle.getLoc():
			return True
		else:
			return False

	def _badCell(self,cell):
		if self._cellOutOfBounds(cell):
			return True
		if self._cellCollidesWithTrail(cell):
			return True
		if self._cellCollidesWithCycle(cell):
			return True
		return False

class LCycleAIRandom:

	def __init__(self, myCycle, theirCycle, boardX, boardY):
		self._myCycle = myCycle
		self._theirCycle = theirCycle
		self._boardX = boardX
		self._boardY = boardY

	def getMove(self):
		
		moveList = ['Straight', 'Right', 'Left']
		
		random.shuffle(moveList)
		
		for move in moveList:
			
			if not self._badCell(self._getCellIfMove(move)):
				return move
		
		return 'Straight'

	def _getCellIfMove(self, move):
		x,y = self._myCycle.getLoc()
		dir = self._myCycle.getDir()
		
		if move == 'Straight':
			x,y = self._updateXY(x,y,dir)
			
		elif move == 'Left':
			if dir == 'N':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'N')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'S')
			else:
				raise Exception('bad direction')
				
		elif move == 'Right':
			if dir == 'N':
				x,y = self._updateXY(x,y,'E')
			elif dir == 'E':
				x,y = self._updateXY(x,y,'S')
			elif dir == 'S':
				x,y = self._updateXY(x,y,'W')
			elif dir == 'W':
				x,y = self._updateXY(x,y,'N')
			else:
				raise Exception('bad direction')
		else:
				raise Exception('bad move')
				
		return [x,y]

	def _updateXY(self, X,Y,dir):
		x,y = X,Y
		if dir == 'N':
			y -= 1
		elif dir == 'E':
			x += 1
		elif dir == 'S':
			y += 1
		elif dir == 'W':
			x -= 1
		else:
			raise Exception('bad direction')
		return [x,y]

	def _cellOutOfBounds(self, cell):
		x,y = cell
		if x < 0 or y < 0:
			return True
		elif x >= self._boardX or y >= self._boardY:
			return True
		return False

	def _cellCollidesWithTrail(self, cell):
		myTrail = self._myCycle.getTrail()
		theirTrail = self._theirCycle.getTrail()
		for t in myTrail:
			if cell == t:
				return True
		for t in theirTrail:
			if cell == t:
				return True
		return False
		
	def _cellCollidesWithCycle(self, cell):
		if cell == self._theirCycle.getLoc():
			return True
		else:
			return False

	def _badCell(self,cell):
		if self._cellOutOfBounds(cell):
			return True
		if self._cellCollidesWithTrail(cell):
			return True
		if self._cellCollidesWithCycle(cell):
			return True
		return False
