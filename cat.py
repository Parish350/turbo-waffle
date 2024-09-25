import pgzrun
import random 

HEIGHT = 600
WIDTH = 500

cat = Actor("cat")
cat.x = WIDTH/2
cat.y = HEIGHT/2

msg = "Move with arrow keys"
def draw():
      screen.blit("green background",(0,0))
      cat.draw()
      screen.draw.text(msg,(50,50))

def update():
  if keyboard.up:
   cat.y -= 5

  if keyboard.down:
   cat.y += 5

  if keyboard.left:
   cat.x -= 5

  if keyboard.right:
   cat.x += 5 

pgzrun.go()
