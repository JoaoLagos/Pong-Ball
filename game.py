import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *

def start(screen):

    """ ITENS DA TELA """
    # BARRA ESQUERDA
    barraEsq = Sprite("assets/game/barra.png")
    barraEsq.x = 10
    barraEsq.y = screen.height/2 - barraEsq.height/2
    # BARRA DIREITA
    barraDir = Sprite("assets/game/barra.png")
    barraDir.x = screen.width - barraEsq.width -10
    barraDir.y = screen.height/2 - barraDir.height/2

    #BALL
    ball = Sprite("assets/game/ball.png")
    ball.x = screen.width/2 - ball.width/2
    ball.y = screen.height/2 - ball.height/2
    """"""""""""""""""""""""""""""""""""

    velBarra = 300
    velBall_X = 350
    velBall_Y = 350

    teclado = Keyboard()

    gameisON= True
    while gameisON:
        screen.set_background_color([0,0,0])
        ball.draw()

        #MOVIMENTAÇÃO BARRA ESQUERDA
        if teclado.key_pressed("W"):
            barraEsq.y -= velBarra*screen.delta_time()
        elif teclado.key_pressed("S"):
            barraEsq.y += velBarra*screen.delta_time()

        #MOVIMENTAÇÃO BOLA
        ball.x += velBall_X*screen.delta_time()
        ball.y += velBall_Y*screen.delta_time()
        ## HORIZONTAL
        ' Ao encostar nas laterais '
        if ball.x <= 0:
            velBall_X = abs(velBall_X)
        elif ball.x >= screen.width-ball.width:
            velBall_X = -velBall_X
        ## VERTICAL
        ' Ao enconstar em cima ou em baixo '
        if ball.y <= 0:
            velBall_Y = abs(velBall_Y)
        elif ball.y >= screen.height-ball.height:
            velBall_Y = -velBall_Y

        if teclado.key_pressed("esc"):
            gameisON = False

        barraEsq.draw()
        barraDir.draw()
        
        screen.update()