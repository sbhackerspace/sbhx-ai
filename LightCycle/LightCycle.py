class LCycle:

    def __init__(self, X=0, Y=0, Dir='E', color=(255,255,255)):
        self._x = X
        self._y = Y
        self._dir = Dir
        self._trail = []
        self._alive = True
        self._color = color

    def isAlive(self):
        return self._alive

    def getLoc(self):
        return [self._x, self._y]
    
    def getColor(self):
        return self._color

    def getDir(self):
        return self._dir

    def getTrail(self):
        return self._trail

    def kill(self):
        self._alive = False
    
    def goStraight(self):
        self._trail.append([self._x, self._y])
        if self._dir == 'N':
            self._y -= 1
        elif self._dir == 'E':
            self._x += 1
        elif self._dir == 'S':
            self._y += 1
        elif self._dir == 'W':
            self._x -= 1
        else:
            raise Exception('bad direction')
            
    def goLeft(self):
        if self._dir == 'N':
            self._dir = 'W'
        elif self._dir == 'E':
            self._dir = 'N'
        elif self._dir == 'S':
            self._dir = 'E'
        elif self._dir == 'W':
            self._dir = 'S'
        else:
            raise Exception('bad direction')
        self.goStraight()

    def goRight(self):
        if self._dir == 'N':
            self._dir = 'E'
        elif self._dir == 'E':
            self._dir = 'S'
        elif self._dir == 'S':
            self._dir = 'W'
        elif self._dir == 'W':
            self._dir = 'N'
        else:
            raise Exception('bad direction')
        self.goStraight()
        