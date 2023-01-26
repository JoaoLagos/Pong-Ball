import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
import random

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

    # LOGO
    logo = Sprite("assets/game/logo.png")
    logo.x = screen.width - logo.width - 60
    logo.y = screen.height - logo.height - 20
    """"""""""""""""""""""""""""""""""""

    velBarraEsq = 300
    velBarraDir = 300
    velBall_X = 365*random.choice([-1, 1])
    velBall_Y = 400*random.choice([-1, 1])
    point_P1 = 0
    point_P2 = 0

    multiplayer = False

    teclado = Keyboard()

    gameisON= True
    while gameisON:
        screen.set_background_color([0,0,0])
        if teclado.key_pressed("ENTER"):
            multiplayer = True


        ######### BARRA #########
        ''' Movimentação da Barra Esquerda: Player 1'''
        move_barra(screen, teclado, barraEsq, velBarraEsq, "W", "S")

        ''' Movimentação da Barra Direita'''
        if not multiplayer: ## Movimentação da Barra PC (IA)
            move_barra_by_IA(screen, ball, barraDir, velBarraDir) # Move barra através de inteligência artificial
        else: ## Movimentação da Barra Direita: Player 2
            move_barra(screen, teclado, barraDir, velBarraDir, "UP", "DOWN")
        ######### FIM BARRA #########


        ######### BOLA #########
        ''' Seta a velocidade X e Y da bola, variando conforme atinge a borda ou a barra, para que não saia da tela '''
        velBall_X, velBall_Y = velBall_by_borders(screen, ball, velBall_X, velBall_Y, barraEsq, barraDir)

        ''' Pontuação GOAL '''
        if ball.x <= 0:
            point_P2 += 1
            ball, velBall_X, velBall_Y = create_ball_after_goal(screen, velBall_X, velBall_Y)
        elif ball.x + ball.width >= screen.width:
            point_P1 += 1
            ball, velBall_X, velBall_Y = create_ball_after_goal(screen, velBall_X, velBall_Y)

        ''' MOVIMENTAÇÃO BOLA '''
        ball.x += velBall_X*screen.delta_time()
        ball.y += velBall_Y*screen.delta_time()
        ######### FIM BOLA #########

        ######### ATALHOS #########
        ''' TELA CHEIA '''
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen() 

        ''' SAIR '''
        if teclado.key_pressed("esc"):
            gameisON = False
        ######### FIM ATALHOS #########

        screen.draw_text(f"Player 1: {point_P1}", x=30, y=30, size=25, color=(255,255,255), bold=True)
        screen.draw_text(f"Player 2: {point_P2}", x= linhaDivisoria.x+linhaDivisoria.width + 30, y=30, size=25, color=(255,255,255), bold=True)    

        logo.draw()
        ball.draw()
        linhaDivisoria.draw()
        barraEsq.draw()
        barraDir.draw()
        
        
        screen.update()


def create_ball_after_goal(screen, velBall_X=0, velBall_Y=0):
    ball = Sprite("assets/game/ball.png")
    ball.x = screen.width/2 - ball.width/2
    ball.y = screen.height/2 - ball.height/2
    velBall_X *= random.choice([-1, 1])
    velBall_Y *= random.choice([-1, 1])

    return ball, velBall_X, velBall_Y

''' Move a barra controlada pelo player '''
def move_barra(screen, teclado, barra, velBarra, bottomUP, bottomDOWN):
    #MOVIMENTAÇÃO BARRA ESQUERDA
    if teclado.key_pressed(bottomUP):
        barra.y -= velBarra*screen.delta_time()
    elif teclado.key_pressed(bottomDOWN):
        barra.y += velBarra*screen.delta_time()

''' Define a velocidade X e Y da bola, quando atinge as bordas ou as barras, para que não saia da tela '''
def velBall_by_borders(screen, ball, velBall_X, velBall_Y, barraEsq, barraDir):#def velBall_by_borders
    '''ballFuturo = Sprite("assets/game/ball.png")
    ballFuturo.x = ball.x + velBall_X*screen.delta_time()
    ballFuturo.y = ball.y + velBall_Y*screen.delta_time()''' # Caso a bola bugue

    ## HORIZONTAL
    ' Ao encostar nas laterais '
    if ball.collided(barraEsq):
        velBall_X = abs(velBall_X)
    elif ball.collided(barraDir):
        velBall_X = -velBall_X
    ## VERTICAL
    ' Ao enconstar em cima ou em baixo '
    if ball.y <= 0:
        velBall_Y = abs(velBall_Y)
    elif ball.y >= screen.height-ball.height:
        velBall_Y = -velBall_Y

    return velBall_X, velBall_Y

''' Move a barra através de inteligência artificial '''
def move_barra_by_IA(screen, ball, barra, velBarra):
    if barra.y + barra.height/2 < ball.y + ball.height/2:
        barra.y += velBarra*screen.delta_time()
    elif barra.y + barra.height/2 > ball.y + ball.height/2:
        barra.y -= velBarra*screen.delta_time()