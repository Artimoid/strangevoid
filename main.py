import pygame
import random
pygame.init()

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("Strange void")

x = 50
y = 50
width = 40
height = 60
vel = 15
r1 = 0;
r2 = 0;
r3 = 0;
r4 = 0;

pygame.mixer.music.load("gamemenu.mp3")
pygame.mixer.music.play(9999)


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill((0,0,0))  
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    r1 = random.randint(1, 640)
    r2 = random.randint(1, 480)
    r3 = random.randint(1, 100)
    r4 = random.randint(1, 102)
    pygame.draw.rect(win, (0,255,0), (r1,r2,r3,r4))
    r1 = random.randint(1, 640)
    r2 = random.randint(1, 480)
    r3 = random.randint(1, 100)
    r4 = random.randint(1, 102)
    pygame.draw.rect(win, (0,0,255), (r1,r2,r3,r4))
    pygame.display.update() 
    
pygame.quit()
