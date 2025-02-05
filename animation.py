import pygame
import time
pygame.init() 

WIDTH =  800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("present.jpg")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
font=pygame.font.SysFont("Times New Roman",72)
text=font.render("Happy Birthday",True,"red")
pic=pygame.image.load("balloons.jpg")
pic=pygame.transform.scale(pic,(WIDTH,HEIGHT))
style=font.render("Have a blast",True,"blue")


run = True
while run:
 screen.fill("White")
 screen.blit(img,(0,0))
 screen.blit(text,(300,300)) 
 pygame.display.update()
 time.sleep(2)
 screen.blit(pic,(0,0))
 screen.blit(style,(300,300))
 pygame.display.update()
 time.sleep(2)
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit() 

