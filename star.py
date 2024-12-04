import pgzrun
import random

HEIGHT = 600
WIDTH = 1000
stars = []
Score = 0
level = 1
players = []
animations = []

    
def update():   
   global stars,level
   if len(stars) == 0:
    make_stars()
    for star in stars:
     duration = 12
     star.anchor = "center","bottom"
     animation = animate(star, duration = duration, y = HEIGHT)

def make_stars():
  global stars,images,level
  star = Actor("star")
  star.x = WIDTH/(level+1)
  stars.append(star)  

def draw():
          screen.blit("space background",(0,0)) 
          for star in stars:
            star.draw()

def on_mouse_down():
        pass   

pgzrun.go()   
