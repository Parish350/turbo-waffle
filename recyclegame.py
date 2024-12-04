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
     animations.append(animation)

def make_players():
  global players,images,level
  player = Actor("bag")
  player.x = WIDTH/(level+2)
  players.append(player)
  for i in range(level):
    option = random.choice(images)
    plr = Actor(option)
    plr.x = (i+1)*(WIDTH/(level+1))
    players.append(plr)
def on_mouse_down(pos):  
  global players,level,Final_level,animations,game_complete,Score
  for player in players:
   if player.collidepoint(pos):
    if "bag" in player.image:
      Score += 10
      if level == Final_level:
            game_complete = True
      else:
          level += 1
          players=[] 
          for animation in animations:
            if animation.running:
             animation.stop()
          animations=[]
pgzrun.go()  
