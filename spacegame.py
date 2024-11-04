import random
import pgzrun

HEIGHT = 600
WIDTH = 500
spaceship = Actor("spaceship")

def draw():
         screen.blit("space background",(0,0))
         spaceship.x = random.randint(50,450)
         spaceship.y = random.randint(50,450)

alienship = Actor("alienship")

def draw():
         alienship.x = random.randint(50,450)
         alienship.y = random.randint(50,450)

alien = Actor("alien")

def draw():
         alien.x = random.randint(50,450)
         alien.y = random.randint(50,450)         