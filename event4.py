import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("ball.png")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
keys = ["uparrow","downarrow","rightarrow","leftarrow"]
font=pygame.font.SysFont("Times New Roman",50)
text=font.render("ball",True,"red")
ballx = 400
bally = 200

run = True
while run:
 screen.fill("White") 
 screen.blit(img,(ballx,bally))
 screen.blit(text,(50,50))
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit() 
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_UP:
          bally -= 10
        if event.key == pygame.K_DOWN:
          bally += 10
        if event.key == pygame.K_RIGHT:   
          ballx += 10
        if event.key == pygame.K_LEFT:
          ballx -= 10
 pygame.display.update()
