import pygame
pygame.init() 

WIDTH =  700
HEIGHT = 700

img = pygame.image.load("blueyspace.png") 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class Player(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()    

sprites = pygame.sprite.Group()
player1 = Player()
sprites.add(player1)

class User(pygame.sprite.Sprite):

   def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("rocketship.png")
        self.image = pygame.transform.scale(self.image,(100,300))
        self.rect = self.image.get_rect()    

user1 = User()
sprites.add(user1)


run = True
while run:
 screen.fill("White")
 screen.blit(img,(0,0)) 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
  if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_UP:
        player1.rect.y -= 10   
     if event.key == pygame.K_DOWN:
        player1.rect.y += 10  
     if event.key == pygame.K_LEFT:
        player1.rect.x -= 10   
     if event.key == pygame.K_RIGHT:
        player1.rect.x += 10             
        player1.rect.y += 0.1
     if event.key == pygame.K_w:
        user1.rect.y -= 10   
     if event.key == pygame.K_a:
        user1.rect.y += 10  
     if event.key == pygame.K_s:
        user1.rect.x -= 10   
     if event.key == pygame.K_d:
      user1.rect.x += 10             
 user1.rect.y += 0.1

    
 sprites.draw(screen) 
 pygame.display.update()
 
