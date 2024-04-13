import pygame as pg
import main

pg.init()

def sprite(image_source, size_x, size_y):
    sprite_sized = pg.transform.scale(pg.image.load(image_source), (size_x, size_y))
    return sprite_sized

sprites = {
    'pl_sprite': 'Game sprites/player.jpg',
}


