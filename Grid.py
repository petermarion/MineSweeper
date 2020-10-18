from Tile import *
import random 

class Grid:
  def __init__(self, difficulty):
    self.height = -1
    self.width = -1
    if difficulty == 1:
      self.height = 8
      self.width = 8
      self.mines = 10
    elif difficulty == 2:
      self.height = 16
      self.width = 16
      self.mines = 40
    else:
      self.height = 16
      self.width = 30
      self.mines = 99

    self.board = [[Tile(-1,-1) for x in range(self.width)] for y in range(self.height)]

    for x in range(self.height):
      for y in range(self.width):
        tile = Tile(x,y)
        self.board[x][y] = Tile(x, y)

    #place the mine 
    for i in range(self.mines):
      x = random.randint(0, self.width-1)
      y = random.randint(0, self.height-1)
      if self.board[x][y].hasBomb == True:
        i-=1
      self.board[x][y].setBomb()
      neighbors = self.getNeighbors(self.getTile(x,y))
      for tile in neighbors:
        tile.bombsNearby += 1

  def getTile(self, x, y):
    return self.board[x][y]

  def place_question_mark(self):  
    pass

  # returns all neighboring tiles
  def getNeighbors(self, tile):
    neighbors = []
    currentX = tile.getX()
    currentY = tile.getY()

    """
    (x-1)(y-1)	(x)(y-1)	(x+1)(y-1)
    (x-1)(y)		(x)(y)		(x+1)(y)
    (x-1)(y+1)	(x)(y+1)	(x+1)(y+1)
    """

    if currentX > 0: #Left neighbors
      neighbors.append(self.getTile(currentX-1, currentY))
      if currentY > 0: #UpLeft
        neighbors.append(self.getTile(currentX-1, currentY-1))
      if currentY < self.height-1: #DownLeft
        neighbors.append(self.getTile(currentX-1, currentY+1))

    if currentX < self.width-1: #Right neighbors
      neighbors.append(self.getTile(currentX+1, currentY))
      if currentY > 0: #UpLeft
        neighbors.append(self.getTile(currentX+1, currentY-1))
      if currentY < self.height-1: #DownLeft
        neighbors.append(self.getTile(currentX+1, currentY+1))

    if currentY > 0: #Up
      neighbors.append(self.getTile(currentX, currentY-1))
    if currentY < self.height-1: #Down
      neighbors.append(self.getTile(currentX, currentY+1))

    return neighbors
#end grid