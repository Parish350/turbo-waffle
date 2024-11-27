import pgzrun
import random

HEIGHT = 500
WIDTH = 800

images = ["battery","bottle","chips","coverbag"] 
Score = 0
level = 1
players = []
animations = []
Final_level = len(images)
game_over = False
game_complete = False
def draw ():
  screen.blit("universe",(0,0))
  for player in players:
     player.draw()

def update():   
   global players,level
   if len(players) == 0:
    make_players()
    for player in players:
     duration = 10
     player.anchor = "center","bottom"
     animation = animate(player, duration = duration, y = HEIGHT)

def make_players():
  global players,images,level
  player = Actor("bag")
  player.x = WIDTH/(level+1)
  players.append(player)  
pgzrun.go()  
