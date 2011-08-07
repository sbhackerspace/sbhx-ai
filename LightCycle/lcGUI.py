import pygame as pg
from pygame.locals import *
import sys

def terminate():
    pg.quit()
    sys.exit()


class lcGUI:
	
	def __init__(self, boardX, boardY, scaleFactor=7, fps=4):
		self._WINDOWWIDTH = boardX * scaleFactor
		self._WINDOWHEIGHT = boardY * scaleFactor
		self._SCALEFACTOR = scaleFactor
		self._FPS = fps

		self._BLACK = (0,0,0)
		self._WHITE = (255,255,255)
		self._RED = (255, 0, 0)
		self._GREEN = (0,255,0)
		self._BLUE = (0, 0, 255)
		
		self._colorList = [self._RED,
					self._GREEN,
					self._BLUE,
					self._WHITE]
		
		#set up pygame and window
		pg.init()

		self._mainClock = pg.time.Clock()
		self._screen = pg.display.set_mode((self._WINDOWWIDTH, self._WINDOWHEIGHT))
		pg.display.set_caption('Light Cycle')

		#set up drawing object
		self._drawObj = Drawer(self._screen, self._SCALEFACTOR)

		# Create a font
		self._font = pg.font.Font(None, 17)

	def handleEvents(self):
		for event in pg.event.get():
			if event.type == QUIT:
				self.terminate()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					self.terminate()
				if event.key == K_p:
					#paused = not paused
					pass
				if event.key == K_RIGHT:
					pass
				if event.key == K_LEFT:
					pass
				if event.key == K_UP:
					pass
				if event.key == K_DOWN:
					pass

	def draw(self, cycleList):
		
			#clear background
			self._screen.fill(self._BLACK)

			for cycle in cycleList:
				#draw the trails
				self._drawObj.drawTrail(cycle)
				#draw the cycle
				self._drawObj.drawCycle(cycle)
			
			#display the FPS
			fps = self._font.render(str(self._mainClock.get_fps()), True, self._WHITE)
			fpsRect = fps.get_rect()
			fpsRect.topleft = [5,5]
			self._screen.blit(fps, fpsRect)
			
			#update the screen
			pg.display.update()
			self._mainClock.tick(self._FPS)
			
	def keyPressed(self):
		for event in pg.event.get():
			if event.type == QUIT:
				self.terminate()
			if event.type == KEYUP:
				return True
		return False
	def terminate(self):
		pg.quit()
		sys.exit()


class Drawer:

	def __init__(self, screen, scaleFactor):
		self._screen = screen
		self._scale = scaleFactor
		self._halfScale = (scaleFactor-1)/2
		
	def drawCycle(self, cycle):
		if cycle.isAlive():
			self._drawCycleAlive(cycle)
		else:
			self._drawCycleDead(cycle)

	def _drawCycleAlive(self, cycle):
		cX, cY = cycle.getLoc()
		cX *= self._scale
		cY *= self._scale
		cDir = cycle.getDir()
		color = cycle.getColor()

		#draw the triangle facing the right direction
		hs = self._halfScale
		if cDir == 'N': 
			pg.draw.line(self._screen, color, (cX-hs, cY+hs), (cX+hs, cY+hs), 1)
			pg.draw.line(self._screen, color, (cX-hs, cY+hs), (cX, cY-hs), 1)
			pg.draw.line(self._screen, color, (cX+hs, cY+hs), (cX, cY-hs), 1)
		elif cDir == 'E': 
			pg.draw.line(self._screen, color, (cX-hs, cY-hs), (cX-hs, cY+hs), 1)
			pg.draw.line(self._screen, color, (cX-hs, cY-hs), (cX+hs, cY), 1)
			pg.draw.line(self._screen, color, (cX-hs, cY+hs), (cX+hs, cY), 1)
		elif cDir == 'S': 
			pg.draw.line(self._screen, color, (cX-hs, cY-hs), (cX+hs, cY-hs), 1)
			pg.draw.line(self._screen, color, (cX-hs, cY-hs), (cX, cY+hs), 1)
			pg.draw.line(self._screen, color, (cX+hs, cY-hs), (cX, cY+hs), 1)
		elif cDir == 'W': 
			pg.draw.line(self._screen, color, (cX+hs, cY-hs), (cX+hs, cY+hs), 1)
			pg.draw.line(self._screen, color, (cX+hs, cY-hs), (cX-hs, cY), 1)
			pg.draw.line(self._screen, color, (cX+hs, cY+hs), (cX-hs, cY), 1)
		else:
			raise

	def _drawCycleDead(self, cycle):
		cX, cY = cycle.getLoc()
		cX *= self._scale
		cY *= self._scale
		cDir = cycle.getDir()
		color = cycle.getColor()
		
		hs = self._halfScale
		
		pg.draw.line(self._screen, color, (cX-hs, cY-hs), (cX+hs, cY+hs), 1)
		pg.draw.line(self._screen, color, (cX+hs, cY-hs), (cX-hs, cY+hs), 1)
		

	def drawTrail(self, cycle):
		firstTime = True
		lastX, lastY = 0,0
		color = cycle.getColor()
		trailThickness = 3
		for tX, tY in cycle.getTrail():
			stX = tX * self._scale
			stY = tY * self._scale
			if firstTime == True:
				firstTime = False
			else:
				pg.draw.line(self._screen, color, (lastX, lastY), (stX, stY), trailThickness)

			lastX, lastY = stX, stY
			
		cX, cY = cycle.getLoc()
		cX *= self._scale
		cY *= self._scale 
		pg.draw.line(self._screen, color, (lastX, lastY), (cX, cY), trailThickness)





