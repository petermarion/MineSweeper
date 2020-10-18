import sys
import pygame
import random
import math
from Tile import *
from Grid import *

#basic parameters
"colors"
Black = (0,0, 0)
White = (255, 255, 255)

Red = (218,63,45)
Green = (53,169,69)
Blue = (65,103,205)
Yellow = (204,204,0)
colors = [Blue, Green, Red, Yellow]
flag_image = pygame.image.load('flag.png')
bomb_image = pygame.image.load('bomb.png')

MARGIN = 10
TILESIZE = 50
X_SCREEN_OFFSET = 0
Y_SCREEN_OFFSET = 200

def click_square():
	"""
	Open clicked square
	"""
	# NOTE: first square clicked is never a bomb and neither will its neighbors
	pass

def isLose():
	"""
	Checks if bomb is clicked (you ded)
	"""
	pass 

def isWin() -> bool:
	"""
	Return True if all non-bomb squares are opened
	"""
	# NOTE: incorrectly marked bombs prevent win
	pass


def bomb_status():
	"""
	Show number of bombs left
	
	"""

	pass

def timer():
	"""
	Timer (max 999 seconds)
	""" 
	pass

def reset():
  pass

#seting up the Mines 

#Uses pygame to create a graphic board
def drawBoard(screen, gameBoard):
  for i in range(gameBoard.height):
    for j in range(gameBoard.width):
      x = (X_SCREEN_OFFSET + MARGIN) + i * (TILESIZE + MARGIN)
      y = (Y_SCREEN_OFFSET + MARGIN) + j * (TILESIZE + MARGIN)
      gameBoard.getTile(i,j).setOriginX(x)
      gameBoard.getTile(i,j).setOriginY(y)
      pygame.draw.rect(screen, White, (x,y,TILESIZE,TILESIZE))

def openTile(screen, gameBoard, tile):
  tilesVisited += 1
  
  posX = tile.getOriginX()
  posY = tile.getOriginY()

  print("opening tile ", tile.getX(), tile.getY())

  pygame.draw.rect(screen, White, (posX,posY,TILESIZE,TILESIZE))

  outcome = tile.reveal()

  if outcome == -1: #Bomb
    font = pygame.font.SysFont(None, 60)
    img = font.render('X', True, Black)
    screen.blit(img, (posX+5, posY+5))
    return
  else: #Empty or Numbered
    font = pygame.font.SysFont(None, 60)
    nearby_bombs = tile.getBombsNearby()
    if nearby_bombs > 0: #Only put num if > 0
      color = nearby_bombs % len(colors)
      img = font.render(str(tile.getBombsNearby()), True, colors[color-1])
      screen.blit(img, (posX+5, posY+5))

    if outcome == 0:
      neighbors = gameBoard.getNeighbors(tile)
      for thisTile in neighbors:
        if not (thisTile.hasBeenSeen()):
          openTile(screen, gameBoard, thisTile)
    
  #end else
  
def run_game():

  difficulty = 1
  #difficulty = 2
  #difficulty = 3
  if difficulty == 1:
    numTiles = 64
    numMines = 10
    numFlags = 10
  elif difficulty == 2:
    numTiles = 256
    numMines = 40
    numFlags = 40
  elif difficulty == 3:
    numTiles = 480
    numMines = 99
    numFlags = 99

  width = TILESIZE * ((numMines + TILESIZE) // MARGIN)
  height = TILESIZE * ((numMines + TILESIZE) // MARGIN)
  tilesVisited = 0


  # Initialize game and create a screen object.
  pygame.init()
  pygame.font.init()
  screen = pygame.display.set_mode((800, 800))
  pygame.display.set_caption("Minesweeper")
  # Start the main loop for the game.
  
  screen.fill(Black)

  
  

  gameBoard = Grid(difficulty)
  drawBoard(screen, gameBoard)
  
  Alive = True    
  # TODO: instead of just drawing new rectangle, draw bomb/empty/nearbyBombs
  while Alive and tilesVisited < numTiles:
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
        #Pygame normally has 0,0 as the coords for top left, for some reason
        #here it sets it to 0,200. X and Y_SCREEN_OFFSET accounts for that
        indexX = (pos[0] - (X_SCREEN_OFFSET + MARGIN)) // (TILESIZE + MARGIN) 
        indexY = (pos[1] - (Y_SCREEN_OFFSET + MARGIN)) // (TILESIZE + MARGIN)
        print("indexX = ", indexX)
        print("indexY = ", indexY)
        
        #if tile is valid index
        if indexX < gameBoard.width and indexY < gameBoard.height:
          tile = gameBoard.getTile(indexX, indexY)
          if event.button == 1: #left click
            openTile(screen, gameBoard, tile)
          elif event.button == 2: #right click
            screen.blit(flag_image, (indexX+5, indexY+5))
      
      pygame.display.flip()
    #end forevent loop
  #end while loop

  if tilesVisited == numTiles:
    print("YOU WIN")

#end run_game


run_game()