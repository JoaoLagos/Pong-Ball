import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *

def start(screen, level):

    ''' ELEMENTOS DA TELA '''
    # LOGO DIFICULDADE
    logoDificuldade = Sprite("assets/dificuldade/dificuldade.png")
    logoDificuldade.x = screen.width/2 - logoDificuldade.width/2
    logoDificuldade.y = 60 

    # BARRA FACIL
    def create_barraFacilOFF():
        barraFacil = Sprite("assets/dificuldade/facil.png")
        barraFacil.x = screen.width/2 - barraFacil.width/2
        barraFacil.y = 300
        return barraFacil
    barraFacil = create_barraFacilOFF()

    # BARRA MEDIO
    def create_barraMedioOFF():
        barraMedio = Sprite("assets/dificuldade/medio.png")
        barraMedio.x = screen.width/2 - barraMedio.width/2
        barraMedio.y = barraFacil.y+barraFacil.height + 30
        return barraMedio
    barraMedio = create_barraMedioOFF()

    #BARRA DIFÍCIL
    ### Fazer !!! ###
    '''def create_barraDificilOFF():
        barraDificil = Sprite("assets/dificuldade/medio.png")
        barraDificil.x = screen.width/2 - barraDificil.width/2
        barraDificil.y = barraMedio.y+barraMedio.height + 30
        return barraDificil
    barraDificil = create_barraDificilOFF()'''

    teclado = Keyboard()
    cursor = Mouse()

    while True:
        screen.set_background_color([0,0,0])

        # BARRA FÁCIL
        if cursor.is_over_object(barraFacil):
            xAux = barraFacil.x
            yAux = barraFacil.y
            barraFacil = Sprite("assets/dificuldade/facil.png") # Colocar o facilON.png (Ainda não foi criado, pois o site Pixelr limitou o número de download)
            barraFacil.x = screen.width/2 - barraFacil.width/2
            barraFacil.y = yAux
            if cursor.is_button_pressed(1):
                level = 1
        else:
            barraFacil = create_barraFacilOFF()
        
        # BARRA MÉDIO
        if cursor.is_over_object(barraMedio):
            xAux = barraMedio.x
            yAux = barraMedio.y
            barraMedio = Sprite("assets/dificuldade/medio.png") # Colocar o medioON.png (Ainda não foi criado, pois o site Pixelr limitou o número de download) 
            barraMedio.x = screen.width/2 - barraMedio.width/2
            barraMedio.y = yAux
            if cursor.is_button_pressed(1):
                level = 2
        else:
            barraMedio = create_barraMedioOFF()

        # BARRA DIFÍCIL
        ### Fazer !!! ###
        '''if cursor.is_over_object(barraDificil):
            xAux = barraDificil.x
            yAux = barraDificil.y
            barraDificil = Sprite("assets/dificuldade/medio.png") # Colocar o medioON.png (Ainda não foi criado, pois o site Pixelr limitou o número de download) 
            barraDificil.x = screen.width/2 - barraDificil.width/2
            barrDificilo.y = yAux
            if cursor.is_button_pressed(1):
                level = 2
        else:
            create_barraDificilOFF()'''


        logoDificuldade.draw()
        barraFacil.draw()
        barraMedio.draw()
        if teclado.key_pressed("ESC"):
            break

        screen.update()
