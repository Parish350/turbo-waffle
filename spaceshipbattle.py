import pygame
pygame.init() 
pygame.mixer.init()
WIDTH =  800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#load the space picture
img=pygame.image.load("blueyspace.png")
redspaceshipx = 600
redspaceshipy = 200
yellowspaceshipx = 200
yellowspaceshipy = 200
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
red_health = 100
yellow_health = 100
winner_text = ""
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

shoot = pygame.mixer.Sound("gunshot.mp3")
hit = pygame.mixer.Sound("grenade.mp3")

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
 red_health_text = HEALTH_FONT.render("Health:" +str(red_health),1,"white")
 yellow_health_text = HEALTH_FONT.render("Health:" +str(yellow_health),1,"white") 
 screen.blit(red_health_text,(500,50))
 screen.blit(yellow_health_text,(100,50))
 pygame.draw.rect(screen,"white",border)
 win_Text = HEALTH_FONT.render(winner_text,1,"white")
 screen.blit(win_Text,(400,300))
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
           shoot.play()   
        if event.key == pygame.K_f:
           bullet = pygame.Rect(RED.x,RED.y,15,5)   
           red_bullets.append(bullet) 
           shoot.play()        

 for bullet in red_bullets:
    bullet.x -= 5
    if YELLOW.colliderect(bullet): 
     red_bullets.remove(bullet)  
     red_health -= 1 
     hit.play()  
 for bullet in yellow_bullets:
    bullet.x += 5   
    if RED.colliderect(bullet): 
     yellow_bullets.remove(bullet)  
     yellow_health -= 1 
     hit.play()    
 if red_health <= 0:
    winner_text = "Yellow Wins!"   
 if yellow_health <= 0:
    winner_text = "Red Wins!"   
 if winner_text != "":   
     break
 pygame.display.update()
 
