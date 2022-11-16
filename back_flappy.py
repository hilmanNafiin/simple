import pygame 
from pygame.locals import*

WIDTH = 480
HEIGHT = 600
FPS = 30

#WARNA

WHITE = (225,225,225)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,225,0)
BLUE = (0,0,225)

#INISIALISAI
pygame.init()

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy bird clone')
clock = pygame.time.Clock()

#game variables
gravity = 0

class Brid(pygame.sprite.Sprite):
    def __init__(Self):
        super().__init__()
        Self.image = pygame.Surface((20, 20))
        Self.image.fill(RED)
        Self.rect = Self.image.get_rect()
        Self.rect.x = 50
        Self.rect.y = HEIGHT // 2
        Self.vy = 0
        
all_sprites = pygame.sprite.Group()
bird = Brid()

all_sprites.add(bird)

run = True
while run :
    clock.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    gravity += 0.25
    bird.rect.y += gravity
    all_sprites.update()
    all_sprites.draw(Screen)
    
    pygame.display.flip()
    
pygame.QUIT