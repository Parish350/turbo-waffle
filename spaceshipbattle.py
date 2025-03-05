import pygame
pygame.init() 
WIDTH =  800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#load the space picture
img=pygame.image.load("blueyspace.png")
redspaceshipx = 600
redspaceshipy = 200
yellowspaceshipx = 200
yellowspaceshipy = 200

border = pygame.Rect(395,0,10,600) 
red = pygame.image.load("redspaceship.png") 
red = pygame.transform.scale(red,(55,40))
red = pygame.transform.rotate(red,90)
RED = pygame.Rect(redspaceshipx,redspaceshipy,55,40)
red_bullets = []
yellow = pygame.image.load("yellowspaceship.png") 
yellow  = pygame.transform.scale(yellow,(55,40))
yellow = pygame.transform.rotate(yellow,270)
YELLOW = pygame.Rect(yellowspaceshipx,yellowspaceshipy,55,40)
yellow_bullets = []


class Spaceship(pygame.sprite.Sprite):
 def __init__(self,x,y,color):
  super().__init__()
  self.x = x
  self.y = y
  self.color = color   
  def display(self):
       pygame.upload.spaceship(screen,self.color,(self.x,self.y))




run = True
while run:
 screen.fill("White") 
 screen.blit(img,(0,0))
 screen.blit(red,(RED.x,RED.y))
 screen.blit(yellow,(YELLOW.x,YELLOW.y))
 pygame.draw.rect(screen,"white",border)
 for bullet in yellow_bullets: 
   pygame.draw.rect(screen,"yellow",bullet)
 for bullet in red_bullets: 
   pygame.draw.rect(screen,"red",bullet)  
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit() 
  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          redspaceshipy -= 10
        if event.key == pygame.K_DOWN:
            redspaceshipy += 10
        if event.key == pygame.K_RIGHT:   
            redspaceshipx += 10
        if event.key == pygame.K_LEFT:
           redspaceshipx -= 10
        if event.key==pygame.K_w:
          yellowspaceshipy -= 10
        if event.key == pygame.K_a:
            yellowspaceshipy += 10
        if event.key == pygame.K_s:   
            yellowspaceshipx += 10
        if event.key == pygame.K_d:
           yellowspaceshipx -= 10  
        if event.key == pygame.K_l: 
           bullet = pygame.Rect(YELLOW.x,YELLOW.y,15,5)
           yellow_bullets.append(bullet)    
        if event.key == pygame.K_f:
           bullet = pygame.Rect(RED.x,RED.y,15,5)   
           red_bullets.append(bullet)      
 pygame.display.update()
 
