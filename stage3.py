import pygame
from pygame import image as img
pygame.init()
bg = img.load('isaac1.jpg')
Pj = img.load('PjIsaac.png')
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.left = False
        self.right = False
    def draw(self, win):
        win.blit(Pj, (self.x, self.y))
win = pygame.display.set_mode((1200,720))
def redibujarpantalla():
    win.blit(bg, (0,bgy))
    win.blit(bg, (0,bgy2))
    tipo.draw(win)
    pygame.display.update()
tipo = player(1280//2, 720//2, 100, 100)
run = True
bgy = 0
bgy2 = (bg.get_height()*-1)
def cambiosalay():
    global bgy
    global  bgy2
    while bgy2 < 0:
        bgy += 10
        bgy2 += 10
        tipo.y += 8
        redibujarpantalla()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and tipo.x > 0:
        tipo.x -= tipo.vel
    elif keys[pygame.K_d] and tipo.x < 1380 - tipo.width:
        tipo.x += tipo.vel
    if keys[pygame.K_w] and tipo.y > 0:
        tipo.y -= tipo.vel
    elif keys[pygame.K_s] and tipo.y < 720 - tipo.height:
        tipo.y += tipo.vel
    if  tipo.y < 110 and tipo.x > (1200//2) - 150 and tipo.x < (1200//2) + 50:
        cambiosalay()

    redibujarpantalla()
pygame.quit()