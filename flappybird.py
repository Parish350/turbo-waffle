import pygame
pygame.init() 
pygame.mixer.init()
WIDTH =  600
HEIGHT = 800


img = pygame.image.load("cloudybackground.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bird = pygame.image.load("bird.png")
pipe = pygame.image.load("pipe.png")

font=pygame.font.SysFont("Times New Roman",50) 
Score = 0
text=font.render(f"Score:{Score}",True,"yellow")
class Bird(pygame.sprite.Sprite):

 def __init__ (self):
        super().__init__()     
        self.image = pygame.image.load("bird.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect() 

birdclass = pygame.sprite.Group()
pipeclass = pygame.sprite.Group()

bird1 = Bird() 
birdclass.add(bird1)


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
     bird1.rect.center = pos  

 birdclass.draw(screen) 
 pipeclass.draw(screen)
 pygame.display.update()
