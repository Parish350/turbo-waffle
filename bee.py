import pgzrun
import random 

HEIGHT = 600
WIDTH = 500

bee = Actor("bee")
bee.x = WIDTH/2
bee.y = HEIGHT/2

msg = "Move with arrow keys"
def draw():
      screen.blit("green background",(0,0))
      bee.draw()
      screen.draw.text(msg,(50,50))

def update():
  if keyboard.up:
   bee.y -= 5

  if keyboard.down:
   bee.y += 5

  if keyboard.left:
   bee.x -= 5

  if keyboard.right:
   bee.x += 5 

pgzrun.go()
