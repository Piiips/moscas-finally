from os import X_OK
from pausa2 import pausa
import pygame
from pygame import image as img
import sys
import random
from pausa2 import *
from Game import *
from pausa2 import *

from pygame import draw

pygame.init()

# imagenes de sprite
# la nave es de autoria propia de nuestro grupo la imagen de fondo y asteroides luego seran actualizadas por imagenes de autoria propibg = img.load('/Users/armon/OneDrive/Escritorio/volas UAI/Programacion/Progamas Py/Proyecto/Fondo weno.jpg')
nav = [img.load('N1.jpg'), img.load('N2.jpg'), img.load('N3.jpg'), img.load('N4.jpg'), img.load('N5.jpg'),
       img.load('N6.jpg'), img.load('N7.jpg'), img.load('N8.jpg'), img.load('N7.jpg'), img.load('N6.jpg'),
       img.load('N5.jpg'), img.load('N4.jpg'), img.load('N3.jpg')]
ast = img.load('Asteroid_Brown.png')
bg = img.load('fondo_anto.jpg')
cr = img.load('corazocito_2_2.png')
tierra = img.load('tierra.jpg')
mal = img.load('planeta_malo.jpg')
# el reloj ayudara a definir la cantidad de fps que contenga el juego
clock = pygame.time.Clock()
# estas dos variables definen la posicion de los fondos
bgY = 0
bgY2 = (bg.get_height() * -1)


# esta clase correspondera a la nave y todas sus caracteristicas7
class nave(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 9
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.timer = 0
        self.hitbox = (self.x, self.y, 105, 105)

    def draw(self, win):
        self.hitbox = (self.x + 9, self.y, 91, 95)
        if self.timer // 2 == 7 or self.timer // 2 == 8 or self.timer // 2 == 6:
            win.blit(nav[self.timer // 2], (self.x, self.y + 8))
        else:
            win.blit(nav[self.timer // 2], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# esta clase correspondera a los proyectiles o disparos que realizaran las naves
class projectile(object):
    def __init__(self, x, y, radius, color, width, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 9
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 3, 25)

    def draw(self, win):
        self.hitbox = (self.x, self.y, 3, 25)
        # pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


# esta clase correspondera a los asteroides y su comportamiento
class asteroid(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 1, self.y + 16, self.width, self.height)
        self.Lp = 2

    def draw(self, win):
        self.hitbox = (self.x + 1, self.y + 16, self.width, self.height)
        pygame.draw.rect(win, (100, 255, 100), (self.x + 1, self.y + 16, self.width, self.height), 2)
        win.blit(ast, (self.x, self.y))

    def colision(self, rect):
        # meteor_hit_list = pygame.sprite.spritecollide(nave, meteor_list, True)
        # hits = pygame.sprite.spritecollide(nave, asteroides, True)
        if rect[1] - rect[3] < self.hitbox[1] and rect[0] < self.hitbox[0] + self.hitbox[2] and rect[0] > self.hitbox[
            0]:
            return True
        return False


class vidas(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(cr, (self.x, self.y))

    def corazones(self):
        x = (cr, (30, 25))
        y = (cr, (65, 25))
        z = (cr, (100, 25))
        a = (cr, (135, 25))
        b = (cr, (170, 25))
        c = (cr, (205, 25))


class fondo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blitear(self, win):
        win.blit(bg, (self.x, self.y))


class ptierra(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blitear(self, win):
        win.blit(tierra, (self.x, self.y))


class pmalo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blitear(self, win):
        win.blit(mal, (self.x, self.y))


cora = []
cx, cy, cz, ca, cb, cc = vidas(30, 25), vidas(64, 25), vidas(100, 25), vidas(135, 25), vidas(170, 25), vidas(205, 25)
cora.append(cx)
cora.append(cy)
cora.append(cz)
cora.append(ca)
cora.append(cb)
cora.append(cc)

# ventana
win = pygame.display.set_mode((1280, 720))
# nombre del juego
pygame.display.set_caption('Moscas Be Like')


# esta funcion correspondera al redibujo de la ventana para actualizar lo que se mostrara por pantalla
def redibujarpantalla():
    global bgY
    global bgY2
    win.fill((0, 0, 0))
    fondo1.blitear(win)
    fondo2.blitear(win)
    for i in cora:
        i.draw(win)
    if len(planetas) == 1:
        if contador == 0:
            planet2.blitear(win)
        else:
            planet1.blitear(win)
    ship.draw(win)
    for j in asteroides:
        if j == asteroide:
            asteroide.draw(win)
        elif j == asteroide2:
            asteroide2.draw(win)
    for blast in blaster:
        blast.draw(win)
    for blast in blaster2:
        blast.draw(win)

    pygame.display.update()


# aca defino algunas variables y creo los objetos basados en las clases anteriores
click = False
speed = 15
blastloop = 0
blaster = []
blaster2 = []
contador = 0
ship = nave(1280 / 2, 600, 100, 100)
asteroide = asteroid(random.randint(0, 690 - 155), bgY, 155, 134)
asteroide2 = asteroid(random.randint(690, 1280 - 155), bgY, 155, 134)
asteroides = []
asteroides.append(asteroide)
asteroides.append(asteroide2)
planet2 = pmalo(540, 400)
planetas = [planet2]
fondo1 = fondo(0, bgY)
fondo2 = fondo(0, bgY2)
planet1 = ptierra(340, -1000)


# main loop o while principal que ejecutara el codigo
#
#
class juego():

    def correr(run):
        blastloop = 0
        bgY = 0
        bgY2 = (bg.get_height() * -1)
        contador = 0
        while run:
            clock.tick(30)
            ship.timer += 1
            if ship.timer >= 26:
                ship.timer = 0
            if planet1.y <= -50:
                fondo1.y += 5
                fondo2.y += 5
            if len(planetas) >= 1:
                if planetas[0] == planet1 and planet1.y <= -50:
                    planet1.y += 5
            planet2.y += 5
            asteroide.y, asteroide2.y = fondo1.y, fondo1.y
            for aster in asteroides:
                if len(blaster) > 0:
                    for i in blaster:
                        if aster.colision(i.hitbox):
                            # asteroides.pop(asteroides.index(aster))
                            aster.Lp -= 1
                            blaster.pop(blaster.index(i))
                    for j in blaster2:
                        if aster.colision(j.hitbox):
                            aster.Lp -= 1
                            blaster2.pop(blaster2.index(j))
                if aster.Lp <= 0:
                    asteroides.pop(asteroides.index(aster))
                if aster.colision(ship.hitbox):
                    cora.pop(0)
                    aster.Lp -= 3
            if fondo1.y > bg.get_height():
                fondo1.y = bg.get_height() * -1
                contador += 1
                asteroide.y, asteroide2.y = bg.get_height() * -1, bg.get_height() * -1
                asteroide.x, asteroide2.x = random.randint(0, 690 - asteroide.width), random.randint(690,
                                                                                                     1280 - asteroide.width)
            if fondo2.y > bg.get_height():
                fondo2.y = bg.get_height() * -1
                if len(asteroides) > 0:
                    asteroides.pop(0)
                if len(asteroides) > 0:
                    asteroides.pop(0)
                if contador <= 2:
                    asteroides.append(asteroide)
                    asteroide.Lp = 2
                    asteroides.append(asteroide2)
                    asteroide2.Lp = 2
                else:
                    planetas.append(planet1)

                if contador == 1:
                    planetas.pop(0)
            keys = pygame.key.get_pressed()
            if blastloop > 0:
                blastloop += 1
            if blastloop > 5:
                blastloop = 0
            if keys[pygame.K_SPACE] and blastloop == 0:
                if len(blaster) < 15:
                    # blaster.append(projectile(round(ship.x + ship.width // 2), round(ship.y + ship.height/2 // 2), 6, (255, 255, 255),))
                    blaster.append(projectile(round(ship.x - 27 + ship.width // 2), round(ship.y + ship.height // 3), 6,
                                              (255, 0, 0), 3, 25))
                    blaster2.append(
                        projectile(round(ship.x + 34 + ship.width // 2), round(ship.y + ship.height // 3), 6,
                                   (255, 0, 0), 3, 25))
                    blastloop += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausa()
            if keys[pygame.K_a] and ship.x > 0:
                ship.x -= ship.vel
                ship.left = True
                ship.right = False
            elif keys[pygame.K_d] and ship.x < 1280 - ship.width:
                ship.x += ship.vel
                ship.left = False
                ship.right = True
            if keys[pygame.K_w] and ship.y > 0:
                ship.y -= ship.vel
                ship.up = True
                ship.down = False
            elif keys[pygame.K_s] and ship.y < 720 - ship.height:
                ship.y += ship.vel
                ship.up = False
                ship.down = True
            for blast in blaster:
                if blast.y < 720 and blast.y > 0:
                    blast.y -= blast.vel
                else:
                    blaster.pop(blaster.index(blast))
            for blast in blaster2:
                if blast.y < 720 and blast.y > 0:
                    blast.y -= blast.vel
                else:
                    blaster2.pop(blaster2.index(blast))

            if len(cora) == 0:
                # hacer reiniciar el juego
                run = False
                cora.append(cx)
                cora.append(cy)
                cora.append(cz)
                cora.append(ca)
                cora.append(cb)
                cora.append(cc)
                ship.x = 1280 / 2
                ship.y = 600
                bgY = 0
                bgY2 = bg.get_height() * -1
                planetas.append(tierra)
                contador = 0
                if len(asteroides) >= 1:
                    asteroides.pop(0)
            redibujarpantalla()
xd = True
juego.correr(xd)