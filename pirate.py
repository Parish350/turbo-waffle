import pygame
import random
pygame.init() 
pygame.mixer.init() 

WIDTH =  700
HEIGHT = 700

img = pygame.image.load("blueyspace.png") 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
stone1 = pygame.image.load("stone1.png")
stone1 = pygame.transform.scale(stone1,(50,50))
stone2 = pygame.image.load("stone2.png")
stone2 = pygame.transform.scale(stone2,(50,50))
stone3 = pygame.image.load("stone3.png")
stone3 = pygame.transform.scale(stone3,(50,50))
images = [stone1,stone2,stone3]
font=pygame.font.SysFont("Times New Roman",50) 
Score = 0
text=font.render(f"Score:{Score}",True,"yellow")

Diamond = pygame.mixer.Sound("diamond.mp3")
Gunshoot = pygame.mixer.Sound("gunshot.mp3")


class Pirate(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("pirate.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()    

pirateclass = pygame.sprite.Group()
soldierclass = pygame.sprite.Group()
gemclass = pygame.sprite.Group()

pirate1 = Pirate()
pirate1.rect.x = random.randint(50,WIDTH-50)
pirate1.rect.y = random.randint(50,HEIGHT-50)
pirateclass.add(pirate1)


class Soldier(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("soldier.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()    

for i in range(5):
 soldier1 = Soldier()
 soldier1.rect.x = random.randint(50,WIDTH-50)
 soldier1.rect.y = random.randint(50,HEIGHT-50)
 soldierclass.add(soldier1)

class Gem(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("stone1.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()    

for i in range(12):
 gem1 = Gem()
 gem1.rect.x = random.randint(50,WIDTH-50)
 gem1.rect.y = random.randint(50,HEIGHT-50)
 gem1.image = random.choice(images)
 gemclass.add(gem1)


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
   pirate1.rect.center = pos 

 pirateclass.draw(screen)
 soldierclass.draw(screen)
 gemclass.draw(screen)
 p_stones = pygame.sprite.spritecollide(pirate1,gemclass,True)
 for stone in p_stones:
    Score += 1
    Diamond.play()
    text=font.render(f"Score:{Score}",True,"yellow")

 s_stones = pygame.sprite.spritecollide(pirate1,soldierclass,True)
 for ruby in s_stones:
    Score -= 1 
    Gunshoot.play() 
    text=font.render(f"Score:{Score}",True,"yellow")
 pygame.display.update()

