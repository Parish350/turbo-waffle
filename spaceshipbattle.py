import pygame
pygame.init() 
WIDTH =  800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#load the space picture
img=pygame.image.load("blueyspace.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

border = pygame.Rect(395,0,10,600) 

scene=pygame.image.load("redspaceship.png") 
pic=pygame.image.load("yellowspaceship.png") 
class Spaceship(pygame.sprite.Sprite):
 def __init__(self,x,y,color):
  super().__init__()


run = True
while run:
 screen.fill("White") 
 screen.blit(img,(0,0))
 pygame.draw.rect(screen,"white",border)
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit() 
 pygame.display.update()
 
