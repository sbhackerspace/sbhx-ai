import unittest
import collisionChecker
import LightCycle

class checkCollision_Test(unittest.TestCase):
	
	def test_checkCollision_leaves_cycles_alive_with_no_collision(self):
		
		cycleList = [LightCycle.LCycle(2, 3, 'E', (255,0,0)), 
				LightCycle.LCycle(5, 4, 'W', (0,255,0))]
		
		boardX, boardY = 100, 100
		
		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		for cycle in cycleList:
			self.assertEquals(cycle.isAlive(), True)

	def test_checkCollision_kills_cycle_if_it_goes_off_the_board_1(self):
		
		cycleList = [LightCycle.LCycle(1, 1, 'W', (255,0,0)), 
				LightCycle.LCycle(5, 4, 'W', (0,255,0))]
		
		boardX, boardY = 100, 100
		cycleList[0].goStraight()
		cycleList[0].goStraight()
		
		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		self.assertEquals(cycleList[0].isAlive(), False)
		self.assertEquals(cycleList[1].isAlive(), True)
		
	def test_checkCollision_kills_cycle_if_it_goes_off_the_board_2(self):
		
		boardX, boardY = 100, 100
		
		cycleList = [LightCycle.LCycle(1, 1, 'W', (255,0,0)), 
				LightCycle.LCycle(3, boardY-2, 'S', (0,255,0))]
		
		cycleList[1].goStraight()
		cycleList[1].goStraight()
		
		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		self.assertEquals(cycleList[0].isAlive(), True)
		self.assertEquals(cycleList[1].isAlive(), False)

	def test_checkCollision_kills_cycle_if_hits_its_own_trail(self):
		
		boardX, boardY = 100, 100
		
		cycleList = [LightCycle.LCycle(1, 1, 'E', (255,0,0)), 
				LightCycle.LCycle(3, 4, 'S', (0,255,0))]
		
		cycleList[0].goStraight()
		cycleList[0].goRight()
		cycleList[0].goRight()
		cycleList[0].goRight()
		
		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		self.assertEquals(cycleList[0].isAlive(), False)
		self.assertEquals(cycleList[1].isAlive(), True)
		
	def test_checkCollision_kills_cycles_if_they_collide(self):
		
		boardX, boardY = 100, 100
		
		cycleList = [LightCycle.LCycle(1, 1, 'E', (255,0,0)), 
				LightCycle.LCycle(3, 1, 'W', (0,255,0))]
		
		cycleList[0].goStraight()
		cycleList[1].goStraight()

		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		self.assertEquals(cycleList[0].isAlive(), False)
		self.assertEquals(cycleList[1].isAlive(), False)
		
	def test_checkCollision_kills_cycle_if_it_collides_with_a_different_trail(self):
		
		boardX, boardY = 100, 100
		
		cycleList = [LightCycle.LCycle(1, 2, 'E', (255,0,0)), 
				LightCycle.LCycle(3, 1, 'S', (0,255,0))]
		
		cycleList[1].goStraight()
		cycleList[1].goStraight()
		cycleList[0].goStraight()
		cycleList[0].goStraight()

		collisionChecker.checkCollision(cycleList, boardX, boardY)
		
		self.assertEquals(cycleList[0].isAlive(), False)
		self.assertEquals(cycleList[1].isAlive(), True)

if __name__ == "__main__":
	unittest.main()