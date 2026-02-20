import pygame
import random
pygame.init() 
pygame.mixer.init()
WIDTH =  1000
HEIGHT = 800


img = pygame.image.load("greenhillbackground.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
sonic = pygame.image.load("sonicrunning.png")
spikesbot = pygame.image.load("spikesbot.png")

font=pygame.font.SysFont("Times New Roman",50) 
Score = 0
text=font.render(f"Score:{Score}",True,"red")
spikesbot_gap = 120
spikesbot_frequency = 1500 #milliseconds
last_spike = pygame.time.get_ticks() -spikesbot_frequency
game_over = False
running = True
class Spike(pygame.sprite.Sprite):

 def __init__ (self,x,y,pos):
        super().__init__()     
        self.image = pygame.image.load("spikesbot.png")
        self.image = pygame.transform.scale(self.image,(100,400))
        self.rect = self.image.get_rect() 
        if pos == 1:
         self.image = pygame.transform.flip(self.image,False,True)
         self.rect.bottomleft= [x,y-int(spikesbot_gap/2)] 
        if pos == -1:
         self.rect.topleft= [x,y+int(spikesbot_gap/2)]  
 def update(self):
  self.rect.x -= 5        
  if self.rect.right < 0:
    self.kill()

class Sonic(pygame.sprite.Sprite):

 def __init__ (self,x,y):
        super().__init__()     
        self.image = pygame.image.load("sonicrunning.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect() 
        self.rect.center = x,y

sonicclass = pygame.sprite.Group()
spikesbotclass = pygame.sprite.Group()

sonic1 = Sonic(100,500)
sonicclass.add(sonic1)


clock = pygame.time.Clock()


run = True
while run:
 clock.tick(60)
 if game_over == False:
   Score = Score+1
   text=font.render(f"Score:{Score}",True,"red") 
   screen.blit(img,(0,0))
   screen.blit(text,(50,50))  
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
     pygame.quit() 
  if event.type == pygame.MOUSEMOTION and game_over == False: 
     pos = pygame.mouse.get_pos()
     sonic1.rect.center = pos 
     running = True 

 if pygame.sprite.groupcollide(sonicclass,spikesbotclass,False,False):   
    game_over = True
    sonic1.rect.center = 10,HEIGHT-50
    running = False 
 if game_over == False and running == True:
    time_now = pygame.time.get_ticks()
    if time_now - last_spike > spikesbot_frequency:
        spike_height = random.randint(-100,100) 
        btm_spikesbot = Spike(WIDTH,int(HEIGHT/2)+spike_height,-1)
        top_spikesbot = Spike(WIDTH,int(HEIGHT/2)+spike_height,1) 
        spikesbotclass.add(btm_spikesbot)
        spikesbotclass.add(top_spikesbot)
        last_spike = time_now
    spikesbotclass.update()
 sonicclass.draw(screen) 
 spikesbotclass.draw(screen)
 pygame.display.update()
