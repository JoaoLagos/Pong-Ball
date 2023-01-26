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

    # LINHA
    linhaDivisoria = Sprite("assets/game/linhaDivisoria.png")
    linhaDivisoria.x = screen.width/2 - linhaDivisoria.width/2
    linhaDivisoria.y = screen.height/2 - linhaDivisoria.height/2
    """"""""""""""""""""""""""""""""""""

    velBarraEsq = 300
    velBall_X = 350
    velBall_Y = 350

    teclado = Keyboard()

    gameisON= True
    while gameisON:
        screen.set_background_color([0,0,0])

        #BARRA
        # Movimentação da Barra Esquerda
        move_barra(screen, teclado, barraEsq, velBarraEsq)
        
        # BOLA
        # Seta a velocidade X e Y da bola, variando conforme atinge a borda, para que não saia da tela
        velBall_X, velBall_Y = velBall_by_borders(screen, ball, velBall_X, velBall_Y)
        #MOVIMENTAÇÃO BOLA
        ball.x += velBall_X*screen.delta_time()
        ball.y += velBall_Y*screen.delta_time()

        if teclado.key_pressed("esc"):
            gameisON = False

        ball.draw()
        linhaDivisoria.draw()
        barraEsq.draw()
        barraDir.draw()
        
        screen.update()

''' Move a barra controlada pelo player '''
def move_barra(screen, teclado, barra, velBarra):
    #MOVIMENTAÇÃO BARRA ESQUERDA
    if teclado.key_pressed("W"):
        barra.y -= velBarra*screen.delta_time()
    elif teclado.key_pressed("S"):
        barra.y += velBarra*screen.delta_time()

''' Define a velocidade X e Y da bola, quando atinge as bordas, para que não saia da tela '''
def velBall_by_borders(screen, ball, velBall_X, velBall_Y):#def velBall_by_borders
    ## HORIZONTAL
    ' Ao encostar nas laterais '
    if ball.x + velBall_X*screen.delta_time() <= 0:
        velBall_X = abs(velBall_X)
    elif ball.x + velBall_X*screen.delta_time() >= screen.width-ball.width:
        velBall_X = -velBall_X
    ## VERTICAL
    ' Ao enconstar em cima ou em baixo '
    if ball.y + velBall_Y*screen.delta_time() <= 0:
        velBall_Y = abs(velBall_Y)
    elif ball.y + velBall_Y*screen.delta_time() >= screen.height-ball.height:
        velBall_Y = -velBall_Y

    return velBall_X, velBall_Y
