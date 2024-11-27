import pgzrun
import random

HEIGHT = 600
WIDTH = 1000
stars = []
for i in range(10):
    star = Actor("star.png")
    star.x = random.randint(50,450)
    star.y = random.randint(50,450)
    stars.append(star)
    

def draw():
          screen.blit("space background",(0,0)) 
          for star in stars:
            star.draw()

def on_mouse_down():
        pass   

pgzrun.go()   
