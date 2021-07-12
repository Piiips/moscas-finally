import pygame
import sys

DISPLAY_W = 1280
DISPLAY_H = 720 
blanco = (255,255,255)
#fuente = pygame.font.SysFont('Consolas', 40)
win = pygame.display.set_mode((1280,720))

def pausa():

    pausa = True
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #Quitar la Pausa
                    pausa = False
                if event.key == pygame.K_ESCAPE:
                    pausa = False
                elif event.key == pygame.K_q: #Salir del juego
                    pygame.quit()
                    quit()

 
        win.fill((0,0,0))
        dibujar_texto('Pausa', 60, blanco, win, 1280/2, (720/2) -50)
        dibujar_texto('Presione Escape o Enter para volver al juego', 40, blanco, win, 1280/2, (720/2) +20)
        dibujar_texto('Presione "Q" para cerrar el juego', 40, blanco, win, 1280/2, (720/2) +70)
        pygame.display.update()

def dibujar_texto(text, size, color, surface ,x ,y):
    font = pygame.font.SysFont('Consolas', size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def draw_cursor():
    cursor_rect= pygame.Rect(0,0,20,20)
    dibujar_texto('π', 38, blanco, win, 880, 330)

        