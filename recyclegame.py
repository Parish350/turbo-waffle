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

def make_players():
  global players,images,level
pgzrun.go()  
