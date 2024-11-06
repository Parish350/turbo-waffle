import random
import pgzrun

HEIGHT = 600
WIDTH = 500
spaceship = Actor("spaceship")
alienship = Actor("alienship")
alien = Actor("alien")
spaceship.x = random.randint(50,450)
spaceship.y = HEIGHT - 200
  
alienship.x = random.randint(50,450)
alienship.y = random.randint(50,450)      
         
alien.x = random.randint(50,450)
alien.y = random.randint(50,450) 
bullets = []   
def draw():
         screen.blit("space background",(0,0))
         spaceship.draw()
         alien.draw()
         alienship.draw()
         for bullet in bullets:
          bullet.draw()     

def update():
 if keyboard.left:
        spaceship.x-=5
 if keyboard.right:
        spaceship.x+=5
def on_key_down(key):
 if key == keys.SPACE:
    bullet = Actor("bullet")
    bullet.y = spaceship.y
    bullet.x = spaceship.x
    bullets.append(bullet)                             
pgzrun.go()