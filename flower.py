import pgzrun
import random

HEIGHT = 600
WIDTH = 500
flow = []
for i in range(10):
    flower = Actor("flower")
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,450)
    flow.append(flower)
    

def draw():
          screen.blit("green background",(0,0)) 
          for flower in flow:
            flower.draw()

def on_mouse_down():
        pass   

pgzrun.go()  