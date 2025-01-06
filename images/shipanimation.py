import random
import pgzrun
import itertools

HEIGHT = 900
WIDTH = 900
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
 (750,50)
]
block_positions = itertools.cycle(BLOCK_POSITIONS)
def move_block():
 animate(
  block,
  'bounce_end',
  duration = 1,
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
 animation = animate(ship, duration = duration, y = HEIGHT,on_finished = handle_gameover)

move_ship()
clock.schedule_interval(move_ship,2)
move_block()
clock.schedule_interval(move_block,2)

pgzrun.go()
