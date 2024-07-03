import random
from sys import exit

import pygame

screen = pygame.display.set_mode((1024, 1024))
pygame.display.set_caption("")
clock = pygame.time.Clock()

enemy_walk1 = pygame.image.load("./images/Enemies/flyFly1.png")
enemy_walk2 = pygame.image.load("./images/Enemies/flyFly2.png")
enemy_walk = [enemy_walk1, enemy_walk2]
enemy_index = 0
enemy_surface = enemy_walk[enemy_index]
enemy_rect = enemy_surface.get_rect(midbottom=(1080, 954))

player_walk1 = pygame.image.load(
    "./images/Player/p1_walk/PNG/p1_walk01.png"
).convert_alpha()
player_walk2 = pygame.image.load(
    "./images/Player/p1_walk/PNG/p1_walk02.png"
).convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load("./images/Player/p1_jump.png").convert_alpha()
player_gravity = 0
player_speed = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 954))


def run():
    started_one = False
    global score_of_player
    global player_gravity
    global player_rect
    global last_click
    global new_click
    global enemy_rect
    run_game = False
    start_time = 0
    pygame.init()
    pygame.font.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if run_game:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if player_rect.bottom == 954:
                            player_gravity = -20
                        else:
                            continue
                    if event.key == pygame.K_ESCAPE:
                        run_game = False
                        run_game = True
                        enemy_rect.left = 1080
                        start_time = int(pygame.time.get_ticks() / 1000)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run_game = True
                        enemy_rect.left = 1080
                        start_time = int(pygame.time.get_ticks() / 1000)
        if run_game is True:
            score_of_player = display_score(start_time)
            started_one = True
            draw_ground()
            draw_player()
            draw_enemy(start_time)
            draw_capitalzation()
            display_score(start_time)
            if enemy_rect.colliderect(player_rect):
                run_game = False
        else:
            if started_one is True:
                screen.fill("Blue")
                scr_font = pygame.font.Font(
                    "./font/BigBlueTerm437NerdFontMono-Regular.ttf", 50
                )
                draw_end_menu()
                scr_fnt = scr_font.render("Fly ate you", False, "Pink")
                scr_rect = scr_fnt.get_rect(midbottom=(524, 524))
                scr_fnt_2 = scr_font.render(
                    f"Your score {score_of_player}", False, "Pink"
                )
                scr_rect_2 = scr_fnt.get_rect(midbottom=(524, 824))
                screen.blit(scr_fnt, scr_rect)
                screen.blit(scr_fnt_2, scr_rect_2)
            else:
                screen.fill("Blue")
                scr_font = pygame.font.Font(
                    "./font/BigBlueTerm437NerdFontMono-Regular.ttf", 50
                )
                draw_start_menu()
                scr_fnt = scr_font.render(
                    "Press space to start and jump", False, "Pink"
                )
                scr_rect = scr_fnt.get_rect(midbottom=(524, 524))
                screen.blit(scr_fnt, scr_rect)
        pygame.display.update()  # draws elements and updates everything
        clock.tick(60)


def draw_start_menu():
    player_stand = pygame.image.load("./images/Player/p1_stand.png").convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center=(524, 624))
    screen.blit(player_stand, player_stand_rect)


def draw_end_menu():
    player_stand = pygame.image.load("./images/Player/p1_hurt.png").convert_alpha()
    player_stand = pygame.transform.scale2x(player_stand)
    player_stand_rect = player_stand.get_rect(center=(524, 624))
    screen.blit(player_stand, player_stand_rect)


def display_score(start):
    current_time = int(pygame.time.get_ticks() / 1000) - start
    scr_font = pygame.font.Font("./font/BigBlueTerm437NerdFontMono-Regular.ttf", 50)
    scr_fnt = scr_font.render(f"{current_time}", False, "Pink")
    scr_rect = scr_fnt.get_rect(midbottom=(524, 624))
    pygame.draw.rect(screen, "gray", scr_rect, 2, 20)
    screen.blit(scr_fnt, scr_rect)
    return current_time


def draw_capitalzation():
    test_font = pygame.font.Font("./font/BigBlueTerm437NerdFontMono-Regular.ttf", 50)
    score = test_font.render("Alien vs Fly", False, "Pink")
    score_rect = score.get_rect(midbottom=(524, 524))
    pygame.draw.rect(screen, "gray", score_rect, 2, 20)
    screen.blit(score, score_rect)


def draw_enemy(start):
    global enemy_index
    global enemy_surface
    global enemy_rect
    time = int(pygame.time.get_ticks() / 1000) - start
    speed = 0
    if time < 5:
        speed = 5
    elif time < 10:
        speed = 7
    elif time < 20:
        speed = 10
    elif time < 30:
        speed = 15
    elif time < 40:
        speed = 20
    elif time < 50:
        speed = 25
    else:
        speed = 27
    enemy_rect.x -= speed
    enemy_index += 0.1
    if enemy_index >= len(enemy_walk):
        enemy_index = 0
    else:
        enemy_surface = enemy_walk[int(enemy_index)]
    screen.blit(enemy_surface, enemy_rect)
    resp_spots = (954, 800)
    if enemy_rect.right <= -5:
        enemy_rect.left = 1090
        enemy_rect.bottom = random.choice(resp_spots)


def draw_player():
    global player_index
    global player_surf
    global player_gravity
    if player_rect.bottom != 954:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        else:
            player_surf = player_walk[int(player_index)]

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 954:
        player_rect.bottom = 954
    if player_rect.left <= 0:
        player_rect.left = 0
    if player_rect.right >= 1024:
        player_rect.right = 1024
    if player_rect.top <= 0:
        player_rect.top = 0
    screen.blit(player_surf, player_rect)


def draw_ground():
    test_surface = pygame.image.load("./images/bg_castle.png").convert_alpha()
    ground = pygame.image.load("./images/Tiles/dirt.png").convert_alpha()
    screen.blit(test_surface, (0, 0))
    screen.blit(test_surface, (256, 0))
    screen.blit(test_surface, (512, 0))
    screen.blit(test_surface, (768, 0))
    screen.blit(test_surface, (1024, 0))
    screen.blit(test_surface, (0, 256))
    screen.blit(test_surface, (256, 256))
    screen.blit(test_surface, (512, 256))
    screen.blit(test_surface, (768, 256))
    screen.blit(test_surface, (1024, 256))
    screen.blit(test_surface, (0, 512))
    screen.blit(test_surface, (256, 512))
    screen.blit(test_surface, (512, 512))
    screen.blit(test_surface, (768, 512))
    screen.blit(test_surface, (1024, 512))
    screen.blit(test_surface, (0, 768))
    screen.blit(test_surface, (256, 768))
    screen.blit(test_surface, (512, 768))
    screen.blit(test_surface, (768, 768))
    screen.blit(test_surface, (1024, 768))
    screen.blit(ground, (0, 954))
    screen.blit(ground, (70, 954))
    screen.blit(ground, (140, 954))
    screen.blit(ground, (210, 954))
    screen.blit(ground, (280, 954))
    screen.blit(ground, (350, 954))
    screen.blit(ground, (420, 954))
    screen.blit(ground, (490, 954))
    screen.blit(ground, (560, 954))
    screen.blit(ground, (630, 954))
    screen.blit(ground, (700, 954))
    screen.blit(ground, (770, 954))
    screen.blit(ground, (840, 954))
    screen.blit(ground, (910, 954))
    screen.blit(ground, (980, 954))
