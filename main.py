import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.mouse import *
import game
import dificuldade

# SCREEN
screen_width = 1920*0.85 # Largura
screen_height = 1080*0.85 # Altura
screen = Window(screen_width, screen_height) # Cria a janela
screen.set_title("Pong Ball") # Título
screen.set_background_color([0,0,0])

# LOGO
logo = Sprite("assets/menu/logo.png")
logo.x = screen.width/2 - logo.width/2 
logo.y = 70

inicio_barras_y = 450
# BARRA JOGAR
def create_barraJogarOFF():
    barraJogar = Sprite("assets/menu/jogar.jpg")
    barraJogar.x = screen.width/2 - barraJogar.width/2
    barraJogar.y = 450
    return barraJogar
barraJogar = create_barraJogarOFF()

# BARRA DIFICULDADE
def create_barraDificuldadeOFF():
    barraDificuldade = Sprite("assets/menu/dificuldade.jpg")
    barraDificuldade.x = screen.width/2 - barraDificuldade.width/2
    barraDificuldade.y = barraJogar.y + 112 + 30
    return barraDificuldade
barraDificuldade = create_barraDificuldadeOFF()

# BARRA SAIR
def create_barraSairOFF():
    barraSair = Sprite("assets/menu/sair.jpg")
    barraSair.x = screen.width/2 - barraSair.width/2
    barraSair.y = barraDificuldade.y + 112 + 30
    return barraSair
barraSair = create_barraSairOFF()

cursor = Mouse()

level = 1

gameIsON = True # Verificador se o jogo está aberto
while gameIsON:

    # BARRA JOGAR
    if cursor.is_over_object(barraJogar):
        xAux = barraJogar.x
        yAux = barraJogar.y
        barraJogar = Sprite("assets/menu/jogarON.jpg")
        barraJogar.x = screen.width/2 - barraJogar.width/2
        barraJogar.y = yAux
        if cursor.is_button_pressed(1):
            game.start(screen)
    else:
        barraJogar = create_barraJogarOFF()

    #BARRA DIFICULDADE
    if cursor.is_over_object(barraDificuldade):
        xAux = barraDificuldade.x
        yAux = barraDificuldade.y
        barraDificuldade = Sprite("assets/menu/dificuldadeON.jpg")
        barraDificuldade.x = screen.width/2 - barraDificuldade.width/2
        barraDificuldade.y = yAux
        if cursor.is_button_pressed(1):
            dificuldade.start(screen, level)  
    else:
        barraDificuldade = create_barraDificuldadeOFF()
    #BARRA DIFICULDADE

    if cursor.is_over_object(barraSair):
        xAux = barraSair.x
        yAux = barraSair.y
        barraSair = Sprite("assets/menu/sairON.jpg")
        barraSair.x = screen.width/2 - barraSair.width/2
        barraSair.y = yAux
        if cursor.is_button_pressed(1):
            gameIsON = False
    else:
        barraSair = create_barraSairOFF()
    
    if pygame.key.get_pressed()[pygame.K_F11]:
        pygame.display.toggle_fullscreen()

    screen.set_background_color([0,0,0])
    logo.draw()
    barraJogar.draw()
    barraDificuldade.draw()
    barraSair.draw()
    
    screen.update()