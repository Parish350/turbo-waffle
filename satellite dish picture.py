import pgzrun
import random

HEIGHT = 600
WIDTH = 500
sats = []
for i in range(10):
    satellitedish = Actor("satellite dish picture")
    satellitedish.x = random.randint(50,450)
    satellitedish.y = random.randint(50,450)
    sats.append(satellitedish)
    

def draw():
          screen.blit("space background",(0,0)) 
          for satellite in sats:
            satellite.draw()

def on_mouse_down():
        pass   

pgzrun.go()       