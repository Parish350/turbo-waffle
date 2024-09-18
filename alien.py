import pgzrun


WIDTH = 600
HEIGHT = 500

alien = Actor("alien")
alien.x = WIDTH/2
alien.y = HEIGHT/2

def draw():
         screen.fill("sky blue")
         alien.draw()






pgzrun.go()