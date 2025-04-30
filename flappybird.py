import pygame
import random
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
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() -pipe_frequency
game_over = False
flying = True
class Pipe(pygame.sprite.Sprite):

 def __init__ (self,x,y,pos):
        super().__init__()     
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect() 
        if pos == 1:
         self.image = pygame.transform.flip(self.image,False,True)
         self.rect.bottomleft= [x,y-int(pipe_gap/2)] 
        if pos == -1:
         self.rect.topleft= [x,y+int(pipe_gap/2)]  
 def update(self):
  self.rect.x -= 5        
  if self.rect.right < 0:
    self.kill()

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

clock = pygame.time.Clock()


run = True
while run:
 if game_over == False:
  Score = Score+1
 text=font.render(f"Score:{Score}",True,"yellow")
 clock.tick(60)
 screen.fill("White")
 screen.blit(img,(0,0))
 screen.blit(text,(50,50))  
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
     pygame.quit() 
  if event.type == pygame.MOUSEMOTION and game_over == False: 
     pos = pygame.mouse.get_pos()
     bird1.rect.center = pos 
     flying = True 

 if pygame.sprite.groupcollide(birdclass,pipeclass,False,False):   
    game_over = True
    bird1.rect.center = 10,HEIGHT-50
    flying = False 
 if game_over == False and flying == True:
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        pipe_height = random.randint(-100,100) 
        btm_pipe = Pipe(WIDTH,int(HEIGHT/2)+pipe_height,-1)
        top_pipe = Pipe(WIDTH,int(HEIGHT/2)+pipe_height,1) 
        pipeclass.add(btm_pipe)
        pipeclass.add(top_pipe)
        last_pipe = time_now
    pipeclass.update()
 birdclass.draw(screen) 
 pipeclass.draw(screen)
 pygame.display.update()
