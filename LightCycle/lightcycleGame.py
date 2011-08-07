#critical support modules. do not modify
import lcGUI
from LightCycle import LCycle as LCycle
import collisionChecker

#AI modules please modify
import basicAI

p1AI = basicAI.LCycleAIHugRight
p2AI = basicAI.LCycleAIHugRight


def movePlayer(cycle, move):
	if move == 'Straight':
		cycle.goStraight()
	elif move == 'Left':
		cycle.goLeft()
	elif move == 'Right':
		cycle.goRight()
	else:
		raise Exception('bad move name')
		
def main():
	#board size
	boardWidth = 40
	boardHeight = 40
	#set up gui
	gui = lcGUI.lcGUI(boardWidth,boardHeight,7, 60) #board width, height, scaleFactor, fps
	
	#set up units
	player1cycle = LCycle(10, 20, 'E', (255,0,0))
	player2cycle = LCycle(30, 20, 'W', (0,255,0))
	cycleList = [player1cycle, player2cycle]

	#setupAI
	player1AI = p1AI(player1cycle, player2cycle, boardWidth, boardHeight)
	player2AI = p2AI(player2cycle, player1cycle, boardWidth, boardHeight)

	gameOver = False
	while not gameOver:

		gui.handleEvents()

		#get player moves
		p1move = player1AI.getMove()
		p2move = player2AI.getMove()
		
		#move players
		movePlayer(player1cycle, p1move)
		movePlayer(player2cycle, p2move)
		
		#check for collisions
		collisionChecker.checkCollision(cycleList, boardWidth,boardHeight)

		#draw to the screen
		gui.draw(cycleList)
		
		#check to see if cycle is dead
		for cycle in cycleList:
			if cycle.isAlive() != True:
				gameOver = True
			
	while not gui.keyPressed():
		pass
	
	return 0

if __name__ == "__main__":
	main()
