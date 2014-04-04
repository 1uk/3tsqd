import pygame
from pygame.locals import *
from Fields import *
from Player import *
from Gui import *

import time

#Steuerungsklasse
class Control(object):

    #Konstruktor
    def __init__(self):
        self.turn = 0

    #Extra Initialisierungsfunktion
    def on_init(self):
        pygame.init()
        self._running = True

        #instantinate gui
        self.g = Gui()

        #instantinate player
        self.p1 = Player(0)
        self.p2 = Player(1)


    #Hauptfunktion (der Anfang & das Ende)
    def on_execute(self):
        #fuehrt on_init() aus und prueft fehler
        if (self.on_init() == False):
            self._running = False

        self.on_render()
        #Laeuft von Anfang bis Objektende
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            #Spielroutine
            self.on_loop()
            #Renderroutine
            self.on_render()

        self.on_cleanup()

    #Verarbeitet Spielerevent
    def on_event(self, event):
        #escape key
        if event.type == KEYDOWN and event.key == 27:
            self._running = False
        elif event.type == MOUSEBUTTONDOWN:
            #left
            if event.button == 1:
                self.on_lbutton_down(event, self.player)


    #Spielroutine
    def on_loop(self):
        self.player = self.turn % 2 + 1
        print self.player

#        self.f.is_field_won()
#        self.f.is_game_won()


    #Renderroutine
    def on_render(self):
        self.g.render_grid()
        pygame.display.update()


    #Aufraeumen (nur ganz am Ende)
    def on_cleanup(self):
        pygame.quit()



    ############
    ## Events ##
    ############

    def on_lbutton_down(self, event, player):
        #event.pos siehe pygame.org/docs/ref/event.html
        if (self.g.get_rect_adress(event.pos[0], event.pos[1])):
            a, b, c, d = self.g.get_rect_adress(event.pos[0], event.pos[1])
            print a, b, c, d
            if (self.g.f[a][b].b[c][d].state == 0):
                self.g.f[a][b].b[c][d].state = player

