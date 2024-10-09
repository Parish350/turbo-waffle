import pgzrun
import random 

HEIGHT = 600
WIDTH = 500

cat = Actor("cat")
cat.x = WIDTH/2
cat.y = HEIGHT/2


flower = Actor("flower")
flower.x = 100
flower.y = 400

Score = 0
Game = True
msg = "Move with arrow keys"
def draw():
      screen.blit("green background",(0,0))
      cat.draw()
      flower.draw()
      screen.draw.text(msg,(50,50))
      screen.draw.text(str(Score),(0,0))
      if Game == False:
         screen.fill("red")
         screen.draw.text("Game Over",(50,50))   
def update():
  global Score
  if keyboard.up:
   cat.y -= 5

  if keyboard.down:
   cat.y += 5

  if keyboard.left:
   cat.x -= 5

  if keyboard.right:
   cat.x += 5 

  if cat.colliderect(flower):
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,450)
    Score += 1 

def time_up(): 
 global Game     
 Game = False 
clock.schedule(time_up,60)
pgzrun.go()