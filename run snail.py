from pygame import*
from sys import*

#def display_score():
#    current_time = time.get_ticks()
#    score_surf = test_font.render(current_time,False,(60,60,60))

def player_animation():
    global player_surf,player_index

    if player_rect.bottom < 380:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_run):player_index = 0
        player_surf = player_run[int(player_index)]


FPS = 65
WIDTH = 750
HEIGHT = 400
TITLE = 'SNAIL RUN'

init()
scr = display.set_mode((WIDTH,HEIGHT))
display.set_caption(TITLE)
display.set_icon(image.load('ww.png'))
clock = time.Clock()
test_font = font.Font(None, 50)
game_active = True


bg_surface = image.load('forest.png').convert_alpha()
ground_surface = image.load('5.png').convert_alpha()
go_surface = image.load('fiv (1).jpg').convert_alpha()
#score_surf = test_font.render('snail run','Arial','black')
#score_rect = score_surf.get_rect(center = (80,20))

snail_surf = image.load('27595460__2_-removebg-preview.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (1100,375))

snail2_surf = image.load('cute__1_-removebg-preview (1).png').convert_alpha()
snail2_rect = snail2_surf.get_rect(bottomright = (1700,375))

raven_surf = image.load('crow-fly-2M7B8EF__1_-removebg-preview.png').convert_alpha()
raven_rect = raven_surf.get_rect(bottomright = (900,170))

player_run1 = image.load('pixil-frame-0 (2) (1) (1).png').convert_alpha()
player_run2 = image.load('snl,frame (1) (2).png').convert_alpha()
player_jump = image.load('pixil-frame-0 (1).png').convert_alpha()
player_run = [player_run2,player_run1]
player_index = 0

player_surf = player_run[player_index]
player_rect = player_surf.get_rect(midbottom = (80,380))
player_gravity = 0

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()

        if e.type == KEYDOWN:
            if e.key == K_SPACE and player_rect.bottom >= 380:
                player_gravity = -9

    if game_active:
        scr.blit(bg_surface,(0,0))
        scr.blit(ground_surface,(0,350))
        #scr.blit(score_surf,score_rect)

        snail2_rect.x -=6.5
        if snail2_rect.right <= -200: snail2_rect.left = 1700
        scr.blit(snail2_surf,snail2_rect)

        snail_rect.x -=6.5
        if snail_rect.right <= -800: snail_rect.left = 1000
        scr.blit(snail_surf,snail_rect)

        raven_rect.x -=6.5
        if raven_rect.right <= 0: raven_rect.left = 900 
        scr.blit(raven_surf,raven_rect)

        player_gravity += 0.3
        player_rect.y += player_gravity
        if player_rect.bottom >= 380: player_rect.bottom = 380
        scr.blit(player_surf,player_rect)  
        

        if snail2_rect.colliderect(player_rect):
            player_rect = player_surf.get_rect(midbottom = (80,380))
            raven_rect = raven_surf.get_rect(bottomright = (900,170))
            snail2_rect = snail2_surf.get_rect(bottomright = (1700,375))
            snail_rect = snail_surf.get_rect(bottomright = (1200,375))

        if snail_rect.colliderect(player_rect):
            player_rect = player_surf.get_rect(midbottom = (80,380))
            raven_rect = raven_surf.get_rect(bottomright = (900,170))
            snail2_rect = snail2_surf.get_rect(bottomright = (1700,375))
            snail_rect = snail_surf.get_rect(bottomright = (1200,375))

        if raven_rect.colliderect(player_rect):
            player_rect = player_surf.get_rect(midbottom = (80,380))
            raven_rect = raven_surf.get_rect(bottomright = (900,170))
            snail2_rect = snail2_surf.get_rect(bottomright = (1700,375))
            snail_rect = snail_surf.get_rect(bottomright = (1200,375))

        display.update()
        clock.tick(FPS)