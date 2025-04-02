import pygame
import random
pygame.init() 

WIDTH =  700
HEIGHT = 700

img = pygame.image.load("universe.png") 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bag = pygame.image.load("bag.png")
box = pygame.image.load("cardboardbox.png")
pencil = pygame.image.load("pencil.png")
images = [bag,box,pencil]
font=pygame.font.SysFont("Times New Roman",50) 
Score = 0
text=font.render(f"Score:{Score}",True,"red")
class Bin(pygame.sprite.Sprite):

 def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("recyclebag.png")
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect() 

binclass = pygame.sprite.Group()
recycleclass = pygame.sprite.Group()
nonrecycle = pygame.sprite.Group()

bin1 = Bin()
binclass.add(bin1)

class Plasticbag(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("coverbag.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()    

for i in range(10):
 plasticbag1 = Plasticbag()
 plasticbag1.rect.x = random.randint(50,WIDTH-50)
 plasticbag1.rect.y = random.randint(50,HEIGHT-50)
 nonrecycle.add(plasticbag1)


class Bag(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("bag.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()    

for i in range(10):
 bag1 = Bag()
 bag1.rect.x = random.randint(50,WIDTH-50)
 bag1.rect.y = random.randint(50,HEIGHT-50)
 bag1.image = random.choice(images)
 recycleclass.add(bag1)

run = True
while run:
 screen.fill("White") 
 screen.blit(img,(0,0))
 screen.blit(text,(50,50)) 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit() 
  if event.type == pygame.MOUSEMOTION: 
    pos = pygame.mouse.get_pos()
    bin1.rect.center = pos

 binclass.draw(screen)
 recycleclass.draw(screen)
 nonrecycle.draw(screen)
 pygame.display.update()

