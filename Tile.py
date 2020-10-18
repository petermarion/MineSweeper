
class Tile():
  x = -1
  y = -1
  originX = 0
  originY = 0
  hasBomb = False
  seen = False
  bombsNearby = 0

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.hasBomb = False
    self.seen = False
  
  def reveal(self):
    self.seen = True
    if self.hasBomb:
      #update sprite to be bomb
      print("you ded")
      return -1 
    elif self.bombsNearby > 0:
      #update sprite to show bombsNearby
      print("a few bombs nearby")
      return self.bombsNearby
    else:
      #update sprite to show empty
      print("this tile empty")
      return 0
  
  def getX(self):
    return self.x

  def setX(self, x):
    self.x = x

  def getOriginX(self):
    return self.originX

  def setOriginX(self, x):
    self.originX = x

  def setOriginY(self, y):
    self.originY = y

  def getOriginY(self):
    return self.originY

  def getY(self):
    return self.y
    
  def setY(self, y):
    self.y = y

  def setBomb(self):
    self.hasBomb = True
    
  def hasBeenSeen(self) -> bool:     
	  return self.seen

  def getBombsNearby(self):
    return self.bombsNearby

  def setBombsNearby(self, numBombs):
    self.bombsNearby = numBombs