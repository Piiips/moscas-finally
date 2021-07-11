import pygame
from pygame.constants import CONTROLLER_AXIS_INVALID
from stage2 import *

class menu():
    def __init__(self, game):
        self.game= game
        self.mid_w= self.game.DISPLAY_W / 2
        self.mid_h= self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect= pygame.Rect(0,0,20,20)
        self.offset = - 100

    def draw_cursor(self): #cursor blanco
        self.game.draw_text('π', 20, self.cursor_rect.x, self.cursor_rect.y)

    def draw_cursor2(self): #cursor negro
        self.game.draw_text2('π', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(menu):
    def __init__(self, game):
        menu.__init__(self, game)
        self.state = 'Start' #empezar
        self.startx = self.mid_w +25
        self.starty = self.mid_h +80 # estos datos son posicion en la pantalla
        self.optionsx = self.mid_w +25
        self.optionsy = self.mid_h +100
        self.creditsx= self.mid_w +25
        self.creditsy = self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.negro)
            self.game.display.blit(self.game.fondo_menu, (0,0))
            self.game.draw_text('Moscas be like', 50, self.game.DISPLAY_W /2, self.game.DISPLAY_H/4) #titulo
            self.game.draw_text('Jugar', 30, self.startx,self.starty)
            self.game.draw_text('Opciones', 25,self.optionsx, self.optionsy)
            self.game.draw_text('Creditos', 25, self.creditsx, self.creditsy)
            self.draw_cursor2()
            self.blit_screen()

    def move_cursor(self):
        if self.game.S_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx +self.offset, self.optionsy)
                self.state = 'Opciones'
            elif self.state == 'Opciones':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.W_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx +self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Opciones'
            elif self.state == 'Opciones':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Opciones':
                self.game.curr_menu = self.game.options
            elif self.state == 'Creditos':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(menu):
    def __init__(self, game):
        menu.__init__(self,game)
        self.state = 'Volumen'
        self.volx = self.mid_w
        self.voly = self.mid_h + 30
        self.controlsx = self.mid_w
        self.controlsy = self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text('Opciones', 60, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -30)
            self.game.draw_text('Volumen', 40, self.volx, self.voly)
            self.game.draw_text('Controles', 40, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            self.game.main_menu
        elif self.game.W_KEY or self.game.S_KEY:
            if self.state == 'Volumen':
                self.state = 'Controles'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controles':
                self.state = 'Volumen'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            #por hacer menu de volumen y controles
            if self.state == 'Controles':
                #self.game.curr_menu = self.game.control
                self.controles()
            elif self.state == 'Volumen':
                pass

    def controles(self):
        si = True
        while si:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                si = False
            #self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text('CONTROLES', 60, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -180)
            self.game.draw_text('E para interactuar', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2)
            self.game.draw_text('W, A, S, D para moverse', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -100)
            self.game.draw_text('ESPACIO para disparar (en la nave)', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -50)
            self.game.draw_text('...', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 +50)
            print('xd')
            #self.draw_cursor()
            self.blit_screen()

class CreditsMenu(menu):
    def __init__(self, game):
        menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.negro)
            self.game.draw_text('Creditos', 75, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -30)
            self.game.draw_text('Hecho por el Grupo H', 50, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 +20) # falta editar
            self.blit_screen()

class Controles(menu):
    def __init__(self, game):
        menu.__init__(self, game)

    def controles(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text('CONTROLES', 60, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 +50)
            self.game.draw_text('E para interactuar', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -50)
            self.game.draw_text('W, A, S, D para moverse', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -100)
            self.game.draw_text('ESPACIO para disparar (en la nave)', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 )
            self.game.draw_text('...', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -150)
            self.draw_cursor()
            self.blit_screen()