import pygame
from PPlay.window import *
from PPlay.sprite import *

# SCREEN
screen_width = 1920*0.85 # Largura
screen_height = 1080*0.85 # Altura
screen = Window(screen_width, screen_height) # Cria a janela
screen.set_title("Pong Ball") # Título