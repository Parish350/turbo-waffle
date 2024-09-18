import pgzrun


WIDTH = 1000
HEIGHT = 1000

player = Actor("player")
player.x = WIDTH/2
player.y = HEIGHT/2

def draw():
         screen.fill("sky blue")
         player.draw()






pgzrun.go()