
def checkCollision(cycleList, boardX, boardY):
	
	for cycle in cycleList:
		if cycle.isAlive():
			if _collisionWithWall(cycle, boardX, boardY):
				cycle.kill()
		if cycle.isAlive():		
			for otherCycle in cycleList: # Check against every other cycle
				if cycle != otherCycle: # Don't check if the cycle has collieded with itself
					if _collisionWith2Cycles(cycle, otherCycle):
						cycle.kill()
				if _collisionWithTrail(cycle, otherCycle):
					cycle.kill()
	
	
def _collisionWithWall(cycle, boardX, boardY):
	x,y = cycle.getLoc()
	collision = False
	if x < 0 or y < 0:
		collision = True
	elif x >= boardX or y >= boardY:
		collision = True
	return collision
	
	
def _collisionWith2Cycles(cycle1, cycle2):
	if cycle1.getLoc() == cycle2.getLoc():
		return True
	else:
		return False
		
def _collisionWithTrail(cycle, trailCycle):
	trail = trailCycle.getTrail()
	cycleLoc = cycle.getLoc()
	for t in trail:
		if cycleLoc == t:
			return True
	return False