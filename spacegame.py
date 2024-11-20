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
aliens = [] 
Score = 0
for i in range(10): 
  alien = Actor("alien")
  alien.x = random.randint(50,450)
  alien.y = random.randint(50,200)
  aliens.append(alien)
Game = True   
def draw():
         screen.blit("space background",(0,0))
         spaceship.draw()
         screen.draw.text(str(Score),(0,0))             
         for alien in aliens:
          alien.draw()
         for bullet in bullets:
          bullet.draw()       
         if Game == False:
          screen.fill("yellow")
          screen.draw.text("Game Over",(50,50))   

def update():
 global Score 
 if keyboard.left:
        spaceship.x-=5
 if keyboard.right:
        spaceship.x+=5  
 if keyboard.up:
        spaceship.y-=5
 if keyboard.down:
        spaceship.y+=5         
 for bullet in bullets:
     bullet.y-=2
     for alien in aliens:      
       if bullet.colliderect(alien):
           bullets.remove(bullet)
           aliens.remove(alien)
           Score += 1
def on_key_down(key):
 if key == keys.SPACE:
    bullet = Actor("bullet")
    bullet.y = spaceship.y
    bullet.x = spaceship.x
    bullets.append(bullet)                             
pgzrun.go()
