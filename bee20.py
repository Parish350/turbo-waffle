import random
import pygame
pygame.init() 
WIDTH =  600
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#load the green picture
img=pygame.image.load("greenbackground.png")
beex = 400
beey = 300
flower1x = 400
flower1y = 300
flower2x = 100
flower2y = 300
flower3x = 400
flower3y =  100
flower4x = 100
flower4y = 100
SCORE_FONT = pygame.font.SysFont('comicsans',40)
bee_Score = 0

bee = pygame.image.load("bee.png") 
bee = pygame.transform.scale(bee,(70,85))
bee = pygame.transform.rotate(bee,360)
BEE = pygame.Rect(beex,beey,40,85)
flower1 = pygame.image.load("flower.png") 
flower1 = pygame.transform.scale(flower1,(70,85))
flower1 = pygame.transform.rotate(flower1,360)
FLOWER1 = pygame.Rect(flower1x,flower1y,40,85)
flower2 = pygame.image.load("flower.png") 
flower2 = pygame.transform.scale(flower2,(70,85))
flower2 = pygame.transform.rotate(flower2,360)
FLOWER2 = pygame.Rect(flower2x,flower2y,40,85)
flower3 = pygame.image.load("flower.png") 
flower3 = pygame.transform.scale(flower3,(70,85))
flower3 = pygame.transform.rotate(flower3,360)
FLOWER3 = pygame.Rect(flower3x,flower3y,40,85)
flower4 = pygame.image.load("flower.png") 
flower4 = pygame.transform.scale(flower4,(70,85))
flower4 = pygame.transform.rotate(flower4,360)
FLOWER4 = pygame.Rect(flower4x,flower4y,40,85)




class Bee(pygame.sprite.Sprite):
 def __init__(self,x,y,color):
  super().__init__()
  self.x = x
  self.y = y
  self.color = color   
  def display(self):
       pygame.upload.bee(screen,self.color,(self.x,self.y))

run = True
while run:
    screen.fill("White") 
    screen.blit(img,(0,0))
    screen.blit(bee,(BEE.x,BEE.y))
    Bee_score = SCORE_FONT.render("Score:" +str(bee_Score),1,"white") 
    screen.blit(Bee_score,(400,50))
    screen.blit(flower1,(FLOWER1.x,FLOWER1.y))
    screen.blit(flower2,(FLOWER2.x,FLOWER2.y))
    screen.blit(flower3,(FLOWER3.x,FLOWER3.y))
    screen.blit(flower4,(FLOWER4.x,FLOWER4.y))
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      pygame.quit() 
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
           BEE.y -= 10
        if event.key == pygame.K_DOWN:
            BEE.y += 10
        if event.key == pygame.K_RIGHT:   
            BEE.x += 10
        if event.key == pygame.K_LEFT:
            BEE.x -= 10

    if BEE.colliderect(FLOWER1):
        FLOWER1.x = random.randint(40,WIDTH-85)
        FLOWER1.y = random.randint(40,HEIGHT-85)
        bee_Score += 1  

    if BEE.colliderect(FLOWER2):
        FLOWER2.x = random.randint(40,WIDTH-85)
        FLOWER2.y = random.randint(40,HEIGHT-85)
        bee_Score += 1  

    if BEE.colliderect(FLOWER3):
        FLOWER3.x = random.randint(40,WIDTH-85)
        FLOWER3.y = random.randint(40,HEIGHT-85)
        bee_Score += 1  
    
    if BEE.colliderect(FLOWER4):
        FLOWER4.x = random.randint(40,WIDTH-85)
        FLOWER4.y = random.randint(40,HEIGHT-85)
        bee_Score += 1   

    pygame.display.update()
