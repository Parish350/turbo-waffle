import pygame
pygame.init() 

WIDTH =  600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
class Rect():
    def __init__ (self,x,y,w,h,color):
      self.x = x
      self.y = y
      self.w = w
      self.h = h
      self.color = color
    def display(self):
      pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
r1 = Rect(10,10,50,50,"red")
r2 = Rect(60,60,100,100,"blue")

class Circle():
    def __init__ (self,x,y,r,color):
      self.x = x
      self.y = y
      self.r = r 
      self.color = color
    def display(self):
       pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)        
cir1 = Circle(300,50,30,"yellow")
cir2 = Circle(200,500,30,"green")

run = True
while run:
 screen.fill("White") 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
 r1.display()   
 r2.display()   
 cir1.display()
 cir2.display()
 pygame.display.update()
 
