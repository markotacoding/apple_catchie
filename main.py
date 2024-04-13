import sys
import pygame as pg
import random as r
import game_logic as gl

pg.init()  # инициализация библиотеки

auto = False

# Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()
speed = 10
player_speed = 0
object_speed = speed

# scores
score, miss = 0, 0
pg.font.init()  # инициализация механизма отображения шрифтов
score_font = pg.font.SysFont('Arial', 32)

# COLORS
GRAY = (237, 237, 237)
RED = (214, 32, 32)
BROWN = (128, 97, 61)

# Game Objects
player = pg.Rect(0, H - 30, 100, 20)  # x, y, width, height
player.centerx = W // 2  # автоматически определить центр игрока по центру экрана
apple = pg.Rect(r.randint(40, W - 40), -50, 40, 40)

# Screen Config
screen = pg.display.set_mode((W, H))  # создаем экран игры размером 1280x720
pg.display.set_caption('Catch an Apple Game')  # название игры в окне игры

# Game loop
game_over = False
while not game_over:  # бесконечный цикл для работы игры
    if miss >= 3:
        game_over = True

    clock.tick(FPS)
    for event in pg.event.get():  # pg.event.get() - обработчик событий в игре
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(GRAY)  # зальем экран серым цветом
    pg.draw.rect(screen, BROWN, player)  # рисую игрового персонажа
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

    if not auto:
        keys = pg.key.get_pressed()  # отслеживаю нажатие кнопок
        if keys[pg.K_LEFT]:
            player_speed = -speed
        elif keys[pg.K_RIGHT]:
            player_speed = speed
        else:
            player_speed = 0
    else:
        if apple.x > player.x:
            player.x += 5
        elif apple.x < player.x:
            player.x -= 5

    gl.player_motion(player, player_speed, W)
