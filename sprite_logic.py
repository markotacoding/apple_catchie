import pygame as pg

pg.init()


def sprite_init(image_source, size_x, size_y):
    sprite_sized = pg.transform.scale(pg.image.load(image_source), (size_x, size_y))
    return sprite_sized


sprites = {
    'pl_sprite': 'main files/Game sprites/player.jpg',
}
