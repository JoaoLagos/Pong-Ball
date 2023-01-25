import pygame
from PPlay.window import *
from PPlay.sprite import *

################### FUNÇÕES #############

# Desenha Barras
''' Função que desenha as barras. Foi criado para não poluir '''
def barrasDraw():
    barraJogar.draw()
    barraDificuldade.draw()
    barraSair.draw()

##########################################

# SCREEN
screen_width = 1920*0.85 # Largura
screen_height = 1080*0.85 # Altura
screen = Window(screen_width, screen_height) # Cria a janela
screen.set_title("Pong Ball") # Título

# LOGO
logo = Sprite("assets/menu/logo.png")
logo.x = screen.width/2 - logo.width/2
logo.y = 70

# BARRA JOGAR
barraJogar = Sprite("assets/menu/jogar.jpg")
barraJogar.x = screen.width/2 - barraJogar.width/2
barraJogar.y = 450

# BARRA DIFICULDADE
barraDificuldade = Sprite("assets/menu/dificuldade.jpg")
barraDificuldade.x = screen.width/2 - barraDificuldade.width/2
barraDificuldade.y = barraJogar.y + barraJogar.height + 30

# BARRA SAIR
barraSair = Sprite("assets/menu/sair.jpg")
barraSair.x = screen.width/2 - barraSair.width/2
barraSair.y = barraDificuldade.y + barraDificuldade.height + 30

gameIsON = True # Verificador se o jogo está aberto
while gameIsON:
    
    


    logo.draw()
    barrasDraw() # Função que desenha as barras. Foi criado para não poluir o while
    screen.update()