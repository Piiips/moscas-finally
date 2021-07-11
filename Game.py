# %%
import pygame
from pygame.mixer import pause
from menu import *
from stage2 import *
from pausa import *
from pygame import image as img
import sys

class Game():
    #weas basicas del propio juego
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.stage = True
        self.W_KEY = False
        self.S_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.QUIT_KEY = False
        self.DISPLAY_W = 1280
        self.DISPLAY_H = 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #self.font_name = 'C:/Users/httpf/OneDrive/Escritorio/Universidad/programacion/Codigos/moscas be like' #xd
        self.font_name = 'Arial'
        #self.font_name = pygame.get_default_font() # por cambiar
        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.fondo_menu = img.load('fondo_menu.jpeg')
        #self.control = Controles(self)
        #self.stage2 = juego(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        if self.playing: #condicion por si muere, resetea el juego y las vidas
            self.stage = True
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            if self.stage:
                self.stage2 = juego.correr(self.stage) #condicion para correr el juego, en este caso stage 2
            self.display.fill(self.negro)
            self.draw_text('Moriste', 20, self.DISPLAY_W/2 ,self.DISPLAY_H/2)
            self.window.blit(self.display,(0,0))
            self.stage = False
            pygame.display.update()
            self.reset_keys()

    #confirmar pulsaciones de teclas
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_w:
                    self.W_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.playing =  True
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True

    #actualizar teclas
    def reset_keys(self):
        self.W_KEY = False
        self.S_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.QUIT_KEY = False

    #dibujar las cosas
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font( None, size) #self.font_name
        text_surface = font.render(text, True, self.blanco)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def draw_text2(self, text, size, x, y):
        font = pygame.font.SysFont( 'Consolas', size) #self.font_name
        text_surface = font.render(text, True, self.negro)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
# %%