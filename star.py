import pgzrun
import random

HEIGHT = 600
WIDTH = 800
stars = []
Score = 0
level = 1
players = []
animations = []
images = ["star"]
Final_level = 5 
def update():   
   global stars,level
   if len(stars) == 0:
    make_stars()
    for star in stars:
     duration = 12
     star.anchor = "center","bottom"
     animation = animate(star, duration = duration, y = HEIGHT)

def draw():
          screen.blit("space background",(0,0)) 
          for star in stars:
            star.draw()
  
def make_stars():
  global stars,images,level
  star = Actor("star")
  star.x = WIDTH/(level+2)
  stars.append(star)
  for i in range(level):
    option = random.choice(images)
    str = Actor(option)
    str.x = (i+1)*(WIDTH/(level+1))
    stars.append(str)
def on_mouse_down(pos):  
  global stars,level,Final_level,animations,game_complete,Score
  for star in stars:
   if star.collidepoint(pos):
    if "star" in star.image:
      Score += 10
      if level == Final_level:
            game_complete = True
      else:
          level += 1
          stars=[] 
          for animation in animations:
            if animation.running:
             animation.stop()
          animations=[]

pgzrun.go()   
