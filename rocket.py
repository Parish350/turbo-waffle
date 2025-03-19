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
player = Player()
sprites.add(player)



run = True
while run:
 screen.fill("White")
 screen.blit(img,(0,0)) 
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
  if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_UP:
        player.rect.y -= 10   
     if event.key == pygame.K_DOWN:
        player.rect.y += 10  
     if event.key == pygame.K_LEFT:
        player.rect.x -= 10   
     if event.key == pygame.K_RIGHT:
        player.rect.x += 10             
 player.rect.y += 0.1

 sprites.draw(screen) 
 pygame.display.update()
 
