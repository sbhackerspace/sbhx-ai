import unittest
import LightCycle

class LCycle_Test(unittest.TestCase):
	
	def test_constructor(self):
		
		startX, startY = 3,4
		dir = 'E'
		color = (255, 0, 0)
		
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		
		self.assertEquals(cycle.isAlive(), True)
		self.assertEquals(cycle.getDir(), dir)
		self.assertEquals(cycle.getLoc(), [startX, startY])
		self.assertEquals(cycle.getColor(), color)
		
	def test_kill_sets_alive_to_false(self):

		cycle = LightCycle.LCycle()
		
		cycle.kill()
		
		self.assertEquals(cycle.isAlive(), False)
		
	def test_goStraight_moves_cycle_in_right_direction_1(self):
		
		startX, startY = 3,4
		dir = 'E'
		color = (255, 0, 0)
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		
		cycle.goStraight()
		
		self.assertEquals(cycle.getDir(), dir)
		self.assertEquals(cycle.getLoc(), [startX+1, startY])
		
	def test_goStraight_moves_cycle_in_right_direction_2(self):
		
		startX, startY = 3,4
		dir = 'N'
		color = (255, 0, 0)
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		
		cycle.goStraight()
		
		self.assertEquals(cycle.getDir(), dir)
		self.assertEquals(cycle.getLoc(), [startX, startY-1])
		
	def test_goLeft_updates_direction_and_location_properly(self):
		
		startX, startY = 3,4
		dir = 'E'
		color = (255, 0, 0)
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		
		cycle.goLeft()
		
		self.assertEquals(cycle.getDir(), 'N')
		self.assertEquals(cycle.getLoc(), [startX, startY-1])
		
	def test_goRight_updates_direction_and_location_properly(self):
		
		startX, startY = 3,4
		dir = 'E'
		color = (255, 0, 0)
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		
		cycle.goRight()
		
		self.assertEquals(cycle.getDir(), 'S')
		self.assertEquals(cycle.getLoc(), [startX, startY+1])
		
	def test_getTrail_returns_true_trail(self):
		
		startX, startY = 3,4
		dir = 'E'
		color = (255, 0, 0)
		cycle = LightCycle.LCycle(startX, startY, dir, color)
		expectedTrail = [[3,4],[4,4],[5,4],[5,3],[6,3]]
		
		cycle.goStraight()
		cycle.goStraight()
		cycle.goLeft()
		cycle.goRight()
		cycle.goStraight()
		
		trail = cycle.getTrail()
		
		self.assertEquals(trail, expectedTrail)
		


if __name__ == "__main__":
	unittest.main()