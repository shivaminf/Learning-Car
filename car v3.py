import pygame
import random

pygame.init()

# screen display property
displayx = 800
displayy = 750
speed_spaceship = 4
speed_enemyship = 3
bg_speed = 5
num_enemy = 3  # number of enemy in a screen frame at a time
pl_blink = 7  # player blink frequency when player get out
pl_blink_time = 30  # no of time to blink whwn player get out

player_car = pygame.image.load('car img/pcar.png')
print(player_car.get_width())
enemyspaceship = pygame.image.load('e_car.png')
e_car1 = pygame.image.load('car img/car1.png')
e_car2 = pygame.image.load('car img/car2.png')
e_car3 = pygame.image.load('car img/car3.png')
e_list = [e_car1,e_car2,e_car3]
background = pygame.image.load('track4.jpg')
player_pixel = [player_car.get_width(),player_car.get_height()]

dspl = pygame.display.set_mode(size=(displayx, displayy))

# title of window
title = pygame.display.set_caption("Car simulation")

# icon to show on window
icon = pygame.image.load('my_logo.png')
pygame.display.set_icon(icon)

# spaceship diplay cars limiting positions
playerx = displayx // 2 - 35
playery = displayy - 90

# Font in pygame
big_game_font = pygame.font.Font('AttackGraffiti.ttf', 40)
small_game_font = pygame.font.Font('AttackGraffiti.ttf', 20)
GREEN = pygame.Color(0, 200, 0)
RED = pygame.Color(200, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(20, 20, 255)
titlee = small_game_font.render('DRIVE THE CAR', True, WHITE)
title_m = titlee.get_rect()
title_m.centerx = 80
title_m.top = 10

title_p = titlee.get_rect()
title_p.centerx = displayx - 100
title_p.top = 10

# point fonts
t_point = big_game_font.render('Q : QUIT', True, GREEN)
title_pt = titlee.get_rect()
title_pt.centerx = displayx // 2
title_pt.top = 10

# main points
t_quit = big_game_font.render('Q : QUIT', True, GREEN)
title_q = titlee.get_rect()
title_q.centerx = displayx // 2
title_q.top = displayy // 2 - 100
t_replay = big_game_font.render('PRESS OTHER KEY TO CONTINUE', True, BLUE)
title_r = titlee.get_rect()
title_r.centerx = displayx // 2 - 200
title_r.top = displayy // 2 - 200


def player(x, y):
    dspl.blit(player_car, (x, y))

def enemy(enemz,x, y):
    dspl.blit(enemz,(x,y))

# points function in pygame
def n_enemy(list):
    point = 0
    for kl in list:
        if kl[1] <= displayy:
            yy = kl[1] + speed_enemyship
            kl.pop(1)
            gl = kl[1]
            kl.pop(1)
            kl.append(yy)
            kl.append(gl)
            enemy(kl[2],kl[0], kl[1])
        else:
            list.remove(kl)
            point = 1
    return point

# lives function
def player_out(list, px, py):
    for i in list:
        enemy_pixelx=i[2].get_width()
        enemy_pixely=i[2].get_height()
        if ((px <= i[0] + enemy_pixelx and px >= i[0]) or (px + player_pixel[0] <= i[0] + enemy_pixelx and px + player_pixel[0] >= i[0])) and ((py <= i[1] + enemy_pixely and py >= i[1]) or (py + player_pixel[1] <= i[1] + enemy_pixely and py + player_pixel[1] >= i[1])):
            return 1

# game starts to execute
def game_menu():
    run1 = True
    clock = pygame.time.Clock()
    while run1:
        dspl.blit(background, (0, 0))
        dspl.blit(t_quit, title_q)
        dspl.blit(t_replay, title_r)
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                run1 = False
                kt = 1
            elif evnt.type == pygame.KEYDOWN:
                kt = 0
                if evnt.key == pygame.K_q:
                    kt = 1
                run1 = False
        pygame.display.update()
        clock.tick(60)
    return kt

# run infinitly before quiting the window for the enemy cars
def main_game():

    run = True
    # enemy
    enemyy1 = 0
    enemyy = 0
    enemyx = displayx // 2 - 32
    speedx = 0
    speedy = 0
    RL = 0  # RIGHT AND LEFT KEY
    UD = 0  # UP AND DOWN KEY
    enemy_list = [[displayx//2-32,-64,e_car1]]
    aa = 0
    kk = 0
    bg = 0
    FPS = 60
    e_pos = [200,347,474,599]
    live = 3
    points = 0
    # starting positions of cars and enemy cars
    playerx = displayx // 2 - 35
    playery = displayy - player_pixel[1] - 2
    clock = pygame.time.Clock()
    while run:
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                run = False

            # speed of spaceship
            if evnt.type == pygame.KEYDOWN:
                if evnt.key == pygame.K_LEFT:
                    speedx = -speed_spaceship
                    RL += 1
                if evnt.key == pygame.K_RIGHT:
                    speedx = speed_spaceship
                    RL += 1
                if evnt.key == pygame.K_UP:
                    speedy = -speed_spaceship
                    UD += 1
                if evnt.key == pygame.K_DOWN:
                    speedy = speed_spaceship
                    UD += 1

            if evnt.type == pygame.KEYUP:
                if (evnt.key == pygame.K_LEFT or evnt.key == pygame.K_RIGHT) and RL == 1:
                    speedx = 0
                    RL = 0
                if (evnt.key == pygame.K_LEFT or evnt.key == pygame.K_RIGHT) and RL == 2:
                    RL = 1
                if (evnt.key == pygame.K_UP or evnt.key == pygame.K_DOWN) and UD == 1:
                    speedy = 0
                    UD = 0
                if (evnt.key == pygame.K_UP or evnt.key == pygame.K_DOWN) and UD == 2:
                    UD = 1

        # dspl.fill((16,26,36))
        bg = bg_speed
        dspl.blit(background, (0, 0))
        # position of spaceship
        playerx += speedx
        playery += speedy

        # boundry of spaceship
        if playerx <= 200 or playerx >= displayx - 190:
            playerx -= speedx
        if playery <= 2 or playery >= displayy - 100:
            playery -= speedy

        # enemy spaceship
        enemyy1 += speed_enemyship
        k = (displayy) // num_enemy
        if enemyy1 // k == 1:
            enemyy1 = 0
            enem_car = random.choice(e_list)
            enemypixel_y = enem_car.get_width()
            enemyx = random.choice(e_pos)
            ll = [enemyx,-1*enemypixel_y,enem_car]
            enemy_list.append(ll)
        data_e = n_enemy(enemy_list)
        # enemy_list = data_e[0]
        # point
        points+=data_e
        t_point = big_game_font.render(f'POINT : {points}', True, WHITE)
        dspl.blit(t_point, title_pt)

        # player position and functionq
        if player_out(enemy_list, playerx, playery) == 1:
            kk = 1
        if kk == 1:
            aa += 1
        if aa % pl_blink == 1:
            player(playerx, playery)
        if aa >= pl_blink * pl_blink_time + 1:
            aa = 0
            kk = 0
        if aa == 0:
            player(playerx, playery)
        if kk==1 and aa==1:
            live -= 1

        lives = f'Live : {live}'
        titlee1 = big_game_font.render(lives, True, RED)
        dspl.blit(titlee1, title_p)
        dspl.blit(titlee, title_m)

        if live == 0:
            run2 = game_menu()
            if run2 == 1:
                run = False
            else:
                main_game()
        pygame.display.update()
        clock.tick(FPS)

main_game()
pygame.quit()
