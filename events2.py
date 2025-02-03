import pygame
WIDTH = 600
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
       pygame.draw.rect(screen,self.color,(self.x,self.y),self.w,self.h)
    def grow(self): 
      self.w += 5 
      self.h += 5
      self.display()         
r1 = Rect(10,10,50,50,"red")
r2 = Rect(60,60,100,100,"blue")
run = True
while run:
 screen.fill("White") 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
  if event.type == pygame.MOUSEBUTTONDOWN:
   r1.display()
   r2.display()
  if event.type == pygame.MOUSEBUTTONUP:
   r1.grow()
   r2.grow()
  if event.type == pygame.MOUSEMOTION:
    pos = pygame.mouse.get_pos()
    r3 = Rect(pos[0],pos[1],4,"Green") 
    r3.display()
 pygame.display.update()
 
