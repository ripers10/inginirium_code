import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 50
x1= 150
y1 = 150
rad = 50
direction = 1
directionY = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + direction
    if x > 500:
        direction = -1
    if x < 0:
         direction = 1

    y1 = y1 + directionY
    if y1 > 500:
        directionY = -1
    if y1 < 0:
         directionY = 1


    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))


    pygame.draw.circle(win, (0, 255, 255), (x1, y1), rad)
    pygame.display.update()

    pygame.time.delay(10)