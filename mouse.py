import pgzrun
import random 

HEIGHT = 600
WIDTH = 500

mouse = Actor("mouse")
mouse.x = WIDTH/2
mouse.y = HEIGHT/2

msg = "Move with arrow keys"
def draw():
      screen.blit("green background",(0,0))
      mouse.draw()
      screen.draw.text(msg,(50,50))

def update():
  if keyboard.up:
   mouse.y -= 5

  if keyboard.down:
   mouse.y += 5

  if keyboard.left:
   mouse.x -= 5

  if keyboard.right:
   mouse.x += 5 

pgzrun.go()
