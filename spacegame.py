import random
import pgzrun

HEIGHT = 600
WIDTH = 500
spaceship = Actor("spaceship")
alienship = Actor("alienship")
alien = Actor("alien")
spaceship.x = random.randint(50,450)
spaceship.y = random.randint(50,450)
        
alienship.x = random.randint(50,450)
alienship.y = random.randint(50,450)      
         
alien.x = random.randint(50,450)
alien.y = random.randint(50,450)   
def draw():
         screen.blit("space background",(0,0))
         spaceship.draw()
         alien.draw()
         alienship.draw()
pgzrun.go()      