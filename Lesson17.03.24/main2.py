import pygame
import random

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
img = pygame.transform.scale(img, (100,100))
all_sprites = pygame.sprite.Group()

for i in range(100):
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = img
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = random.randrange(w)
    sprite.rect.y = random.randrange(h)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))
    all_sprites.draw(win)
    pygame.display.update()
