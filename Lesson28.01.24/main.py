import pygame

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

xCircle = width / 2
yCircle = height / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xCircle -= 5
    elif keys[pygame.K_RIGHT]:
        xCircle += 5
    elif keys[pygame.K_UP]:
        yCircle -= 5
    elif keys[pygame.K_DOWN]:
        yCircle += 5


    win.fill((255,255,255))
    pygame.draw.circle(win, (255,0,0), (xCircle, yCircle), 30)

    pygame.display.update()

    pygame.time.delay(10)