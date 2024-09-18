import pgzrun


WIDTH = 500
HEIGHT = 500

player = Actor("player")
player.x = WIDTH/2
player.y = HEIGHT/2

msg = "Click on the Player"
def draw():
         screen.fill("sky blue")
         player.draw()
         screen.draw.text(msg,(50,50))

def on_mouse_down(pos):
 global msg 
 if player.collidepoint(pos):
     player.x= random.randint(50,550)
     player.y= random.randint(50,450)
     msg = "Player found"

 else:
      msg = "Player not found"

pgzrun.go()
