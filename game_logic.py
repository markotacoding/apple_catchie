import random as r
import pygame as pg


def player_motion(obj, sp, s_width):
    obj.x += sp

    if obj.left <= 0:  # если координата левого края объекта меньше/равна нулю
        obj.left = 0  # зафиксировать координату левого края объекта в нуле
    elif obj.right >= s_width:  # если координата правого края объекта больше/равна ширине экрана
        obj.right = s_width  # зафиксировать координату правого края объекта на ширине экрана


def opponent_motion(obj, sp, s_width, s_height, pl):
    obj.y += sp * 0.7
    if obj.bottom > s_height:  # если координата нижнего края яблока больше высоты экрана
        obj.x = r.randint(40, s_width - 40)  # поменять яблоку Х
        obj.y = -50  # поменять яблоку У
        return 'miss'
    elif obj.colliderect(pl):
        obj.x = r.randint(40, s_width - 40)  # поменять яблоку Х
        obj.y = -50  # поменять яблоку У
        return 'catch'


def draw_button(screen, text, x, y, w, h, color):
    mouse_pos = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    btn_rect = pg.Rect(x // 2, y, w, h)
    btn_rect_center = (x, y + 30)
    if btn_rect.collidepoint(mouse_pos):
        if click[0]:
            return "Continue"
        color = (color[0] - 50, color[1] - 50, color[2] - 50)
    pg.draw.rect(screen, color, btn_rect)
    text_init = text.render('Continue', True, (0, 0, 0))
    text_rect = text_init.get_rect(center=btn_rect_center)
    screen.blit(text_init, text_rect)

def draw_game_over_button(screen, text, x, y, w, h, color):
    mouse_pos = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    btn_rect = pg.Rect(x // 2, y, w, h)
    btn_rect_center = (x, y + 30)
    if btn_rect.collidepoint(mouse_pos):
        if click[0]:
            return "gmv"
        color = (color[0] - 50, color[1] - 50, color[2] - 50)
    pg.draw.rect(screen, color, btn_rect)
    text_init = text.render('Restart?', True, (0, 0, 0))
    text_rect = text_init.get_rect(center=btn_rect_center)
    screen.blit(text_init, text_rect)
