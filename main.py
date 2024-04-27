import sys
import os
import pygame as pg
import random as r
import game_logic as gl
import sprite_logic as spt
from highscore_save import save as s
from highscore_save import download as d
from highscore_save import find as f
pg.init()
def restart():
    main()
def main():
    W = 1280
    H = 720
    FPS = 60
    clock = pg.time.Clock()
    speed = 10
    player_speed = 0
    object_speed = speed

    screen = pg.display.set_mode((W, H))  # создаем экран игры размером 1280x720
    pg.display.set_caption('Catch an Apple Game')

    score, miss = 0, 0
    f('highscore.txt')
    if f('highscore.txt') == True:
        highscore = d('highscore.txt')
    elif f('highscore.txt') == False:
        s('hs', 'highscore.txt', "0", 'main files/')
        highscore = d('highscore.txt')
    pg.font.init()
    score_font = pg.font.SysFont('Arial', 32)

    GRAY = (237, 237, 237)
    RED = (214, 32, 32)
    BROWN = (128, 97, 61)
    BLACK = (0, 0, 0, 50)

    player = spt.sprite_init(spt.sprites['pl_sprite'], 125, 100).get_rect()
    player_img = spt.sprite_init(spt.sprites['pl_sprite'], 125, 146.5)
    player.y = H - 60

    player.centerx = W // 2
    apple = pg.Rect(r.randint(40, W - 40), -50, 40, 40)

    pause = False
    pause_origin = False

    # Game loop
    game_over = False
    while not game_over:  # бесконечный цикл для работы игры

        clock.tick(FPS)
        for event in pg.event.get():  # pg.event.get() - обработчик событий в игре
            if event.type == pg.QUIT:
                hs = score
                if hs <= highscore:
                    hs = highscore
                hs_data = f'{hs}'
                s(f'hs', 'highscore.txt', hs_data, 'main files/')
                pg.quit()
                sys.exit()

        if pause == True:
            object_speed = 0
            player_speed = 0
            pg.draw.rect(screen, BLACK, pg.Rect(0, 0, W, H))
            gl.draw_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY)
            pg.display.update()
            if gl.draw_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY) == "Continue":
                pause = False
                object_speed = speed
        elif miss == 3:
            hs = score
            if hs <= highscore:
                hs = highscore
            hs_data = f'{hs}'
            s(f'hs', 'highscore.txt', hs_data, 'main files/')
            object_speed = 0
            player_speed = 0
            pg.draw.rect(screen, BLACK, pg.Rect(0, 0, W, H))
            gl.draw_game_over_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY)
            if gl.draw_game_over_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY) == 'gmv':
                restart()
            pg.display.update()
        else:
            screen.fill(GRAY)  # зальем экран серым цветом
            screen.blit(player_img, player)
            pg.draw.ellipse(screen, RED, apple)  # рисую яблоко
            score_text = score_font.render(f'Score: {score}', True, (107, 237, 185))
            miss_text = score_font.render(f'Miss: {miss}', True, (107, 237, 185))
            highscore_text = score_font.render(f'Highscore: {highscore}', True, (107, 237, 185))
            screen.blit(score_text, (10, 10))  # расположить score_text в координатах 10;10
            screen.blit(miss_text, (10, 40))
            screen.blit(highscore_text, (10, 70))

            pg.display.update()  # обновление экрана игры

            apple_catch = gl.opponent_motion(apple, object_speed, W, H, player)
            if apple_catch == 'miss':
                miss += 1
            elif apple_catch == 'catch':
                score += 10
            keys = pg.key.get_pressed()  # отслеживаю нажатие кнопок
            if keys[pg.K_LEFT]:
                player_speed = -speed
            elif keys[pg.K_RIGHT]:
                player_speed = speed
            elif keys[pg.K_ESCAPE]:
                pause = True
            else:
                player_speed = 0

            gl.player_motion(player, player_speed, W)
main()
