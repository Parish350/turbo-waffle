import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("bulb.png")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
font=pygame.font.SysFont("Times New Roman",72)
text=font.render("Off",True,"yellow")
pic=pygame.image.load("light bulb.png")
pic=pygame.transform.scale(pic,(WIDTH,HEIGHT))
style=font.render("On",True,"green")

run = True
while run:
 screen.fill("White") 
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit() 
    if event.type == pygame.MOUSEBUTTONDOWN:   
       screen.blit(pic,(0,0))
       screen.blit(style,(50,50))
       pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
      screen.blit(img,(0,0))
      screen.blit(text,(50,50))
      pygame.display.update()
 
