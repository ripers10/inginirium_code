import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
x = 0
y = 0
w = 150
h = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 255, 255)
    win.fill(color)
    pygame.draw.rect(win, (255, 255, 0),)



    pygame.display.update()





