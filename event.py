import pygame
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
class Circle():
    def __init__ (self,x,y,r,color):
      self.x = x
      self.y = y
      self.r = r 
      self.color = color
    def display(self):
       pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)
    def grow(self): 
      self.r += 5 
      self.display()         
cir1 = Circle(300,50,30,"yellow")
cir2 = Circle(400,70,50,"green")
run = True
while run:
 screen.fill("White") 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
  if event.type == pygame.MOUSEBUTTONDOWN:
   cir1.display()
   cir2.display()
  if event.type == pygame.MOUSEBUTTONUP:
   cir1.grow()
   cir2.grow()
  if event.type == pygame.MOUSEMOTION:
    pos = pygame.mouse.get_pos()
    cir3 = Circle(pos[0],pos[1],4,"Red") 
    cir3.display()
 pygame.display.update()
 
