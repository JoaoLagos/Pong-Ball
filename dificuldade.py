import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *

def start(screen):
    barraFacil = Sprite("assets/dificuldade/facil.png")
    barraFacil.x = screen.width/2 - barraFacil.width/2
    barraFacil.y = 300

    teclado = Keyboard()

    while True:
        screen.set_background_color([0,0,0])


        barraFacil.draw()
        if teclado.key_pressed("ESC"):
            break

        screen.update()
