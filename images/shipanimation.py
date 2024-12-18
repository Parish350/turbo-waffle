import random
import pgzrun
import itertools

HEIGHT = 700
WIDTH = 800
block = Actor('block')
block.x = 400
block.y = 400
ship = Actor('ship')
ship.x = 500
ship.y = 500
BLOCK_POSITIONS = [
 (50,50), 
 (750,650),
 (50,650),
 (750,50),
]
block_positions = itertools.cycle(BLOCK_POSITIONS)
def move_block():
 animate(
  block,
  'bounce_end',
  duration=1,
  pos=next(block_positions)
 )

def move_ship():
    x = random.randint(750,50)
    y = random.randint(50,60)
    ship.target = x,y
def draw():
 screen.fill("blue")
 block.draw()
 ship.draw()


move_block()
clock.schedule_interval(move_block,2)
pgzrun.go()
