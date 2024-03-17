import pygame

pygame.init()
size = w,h = 700, 700
FPS = 30
win = pygame.display.set_mode(size)

img = pygame.image.load('inzh.png')

def load_image(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0,0))
    img.set_colorkey(colorkey)
    return img

img = pygame.image.load('inzh.png')
img1 = pygame.transform.scale(img, (200,200))
img2 = pygame.transform.scale(img, (700,700))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    win.fill('#dbf6e9')
    win.blit(img1, (0,0))
    win.blit(img2, (100,200))
    pygame.display.update()
