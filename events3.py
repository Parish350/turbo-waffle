import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("rocket.png")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
keys = ["uparrow","downarrow","rightarrow","leftarrow"]
font=pygame.font.SysFont("Times New Roman",72)
text=font.render("press arrow key to move rocket",True,"blue")
rocketx = 400
rockety = 200

run = True
while run:
 screen.fill("White") 
 screen.blit(img,(rocketx,rockety))
 screen.blit(text,(50,50))
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit() 
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_UP:
          rockety -= 5  
        if event.key == pygame.K_DOWN:
            rockety += 5
        if event.key == pygame.K_RIGHT:   
            rocketx += 5
        if event.key == pygame.K_LEFT:
            rocketx -= 5
 pygame.display.update()
