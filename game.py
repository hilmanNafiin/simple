import pygame 
import sys
from random import choice
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
Background_sound = pygame.mixer.Sound('Last-Friday-Night.mp3')
bg_image = pygame.image.load('bg_image.png')
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
Background_sound.play()

pygame.display.set_caption('Flappy bird clone')
clock = pygame.time.Clock()

#GAME VARIABLES
gravity = 0
score = 0
pos_list = [[-300,350],[-400,250],[-200,450],[-450,150],[-50,550]]


def create_Pipa():
    y_pos = choice(pos_list)
    p1 = Top(y_pos[0])
    p2 = Bottom(y_pos[1])
    detection = DetectionPoint(p2.rect.x, y_pos[1])
    Pipas.add(p1)
    Pipas.add(p2)
    all_sprites.add(p1)
    all_sprites.add(p2)
    detect_group.add(detection)
    all_sprites.add(detection)

def show_text(text, font_size, font_color, x, y):
    font = pygame.font.SysFont(None,font_size)
    font_surface= font.render(text,True, font_color)
    Screen.blit(font_surface,(x,y))
    
    
def game_over_screen():
    Screen.fill(BLACK)
    show_text("GAME OVER", 40, RED, WIDTH//2 - 65, HEIGHT//4)
    show_text("YOU SCORE = {}".format(score),25, WHITE, WIDTH//2 - 50, HEIGHT//2 + 100)
    Background_sound.stop()
    sound_game_over.play()
    show_text("Press any key to Continue",25, WHITE, WIDTH//2 - 95, HEIGHT//4 + 50)
    
    
    
    
    pygame.display.flip()
    waiting_game_over = True
    while waiting_game_over:
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYUP:
                waiting_game_over = False
                Background_sound.stop()
                sound_game_over.play()

class Brid(pygame.sprite.Sprite):
    def __init__(Self):
        super().__init__()
        Self.imagee = pygame.image.load('planeRed2.png')
        Self.image = pygame.transform.scale(Self.imagee, (30, 30))
        Self.rect = Self.image.get_rect()
        Self.rect.x = 50
        Self.rect.y = HEIGHT // 2
        
    def update(Self):
        global game_over
        if Self.rect.y <= 0:
            Self.rect.y = 0
        if Self.rect.y > HEIGHT:
            game_over = True
        
        
class Pipa(pygame.sprite.Sprite):
    def __init__(Self):
        super().__init__()
        Self.image = pygame.Surface((20,500))
        Self.image.fill(GREEN)
        Self.rect = Self.image.get_rect()
        Self.rect.x = 400
        
    def update(Self):
        Self.rect.x -= 4
        if Self.rect.x < -20:
            Self.kill()
            
        
class Top(Pipa):
    def __init__(Self, y):
        super().__init__()
        Self.rect.y = y
        
class Bottom(Pipa):
    def __init__(Self, y):
        super().__init__()
        Self.rect.y = y
    
class DetectionPoint(pygame.sprite.Sprite):
    def __init__(Self, x,y):
        super().__init__()
        Self.image = pygame.Surface((20,120))
        Self.image.set_colorkey(BLACK)
        Self.rect = Self.image.get_rect()
        Self.rect.x = x
        Self.rect.bottom = y
        Self.hit = False
        
    def update(Self):
        Self.rect.x -= 4
        if Self.rect.x < -20:
            Self.kill()

#LOAD SOUND
score_sound = pygame.mixer.Sound('retro.wav')
sound_game_over = pygame.mixer.Sound('sound_GO.wav')
        
all_sprites = pygame.sprite.Group()
Pipas = pygame.sprite.Group()
detect_group = pygame.sprite.Group()
bird = Brid()

create_Pipa()
all_sprites.add(bird)

#LOOPING
game_over = False
run = True
while run :
    if game_over:
        game_over_screen()
        all_sprites = pygame.sprite.Group()
        Pipas = pygame.sprite.Group()
        detect_group = pygame.sprite.Group()
        bird = Brid()
        Background_sound.play()
        
        
        create_Pipa() 
        
        all_sprites.add(bird) 
        score = 0
        game_over = False
    clock.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:   
                if event.key == K_SPACE:
                    # Background_sound.play()
                    gravity = 0
                    gravity -= 10
            
    gravity += 0.50
    bird.rect.y += gravity 
    # Background_sound.play()
            
            #check bird dengan detection point (score) 
    bird_hit_point = pygame.sprite.spritecollide(bird,detect_group,False)
    if bird_hit_point and not bird_hit_point[0].hit:
                score += 1
                bird_hit_point[0].hit = True
                score_sound.play()
            
            #check coletion  bird dengan
    bird_hit_Pipa = pygame.sprite.spritecollide(bird,Pipas,False)
    if bird_hit_Pipa:
                Background_sound.stop()
                game_over = True
                sound_game_over.play()
                            

    if len(Pipas) <= 0:
                create_Pipa()
                
                
    all_sprites.update()
    sound_game_over.stop()
    Screen.fill(BLACK)
    all_sprites.draw(Screen)
    show_text(str(score), 32, WHITE,WIDTH//2, HEIGHT//4 - 100)
            
    pygame.display.flip()

pygame.QUIT