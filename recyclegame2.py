import pygame
pygame.init() 

WIDTH =  700
HEIGHT = 700

img = pygame.image.load("universe.png") 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
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
        self.image = pygame.transform.scale(self.image,(100,120))
        self.rect = self.image.get_rect()    

plasticbag1 = Plasticbag()
nonrecycle.add(plasticbag1)


class Bag(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("bag.png")
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()    

bag1 = Bag()
recycleclass.add(bag1)

run = True
while run:
 screen.fill("White") 
 screen.blit(img,(0,0)) 
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

