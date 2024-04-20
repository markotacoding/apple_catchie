import sys
import pygame as pg
import random as r
import game_logic as gl
import sprite_logic as spt

pg.init()

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
    if miss == 3:
        object_speed = 0
        player_speed = 0
        pg.draw.rect(screen, BLACK, pg.Rect(0, 0, W, H))
        gl.draw_game_over_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY)
        if gl.draw_game_over_button(screen, score_font, W // 2, H // 2 - 20, W * 0.5, H * 0.07, GRAY) == 'gmv':
            pass
        pg.display.update()
    else:
        screen.fill(GRAY)  # зальем экран серым цветом
        screen.blit(player_img, player)
        pg.draw.ellipse(screen, RED, apple)  # рисую яблоко
        score_text = score_font.render(f'Score: {score}', True, (107, 237, 185))
        miss_text = score_font.render(f'Miss: {miss}', True, (107, 237, 185))
        screen.blit(score_text, (10, 10))  # расположить score_text в координатах 10;10
        screen.blit(miss_text, (10, 40))

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
