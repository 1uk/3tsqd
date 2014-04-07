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
        self.p = []
        for i in range(2):
            self.p.append(Player(i))

        self.turn = 0


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
            #self.on_loop()
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
                self.on_lbutton_down(event)


    #Spielroutine
    def on_loop(self):
        pass

    #Renderroutine
    def on_render(self):
        self.g.render_grid()
        pygame.display.update()


    #Aufraeumen (nur ganz am Ende)
    def on_cleanup(self):
        pygame.quit()

    def gameturn(self, address):
        a, b, c, d = address
        if (self.g.f[a][b].b[c][d].state == 0):
            #fill it
            self.g.f[a][b].b[c][d].state = self.p[self.turn%2].p_id + 1

        #if the field is won
#        if self.g.f[a][b].is_won():
#            self.g.won_fields.append((a, b))
#            if is_game_won():
#                self.game_won(player)

        self.turn += 1
        self.player = self.turn % 2 + 1
        self.on_render()

    def is_game_won(self):
        self.g.is_grid_won()




    ############
    ## Events ##
    ############
    #siehe pygame.org/docs/ref/event.html
    #------------------------------------

    def on_lbutton_down(self, event):
        #if a rect is clicked
        if (self.g.get_rect_adress(event.pos[0], event.pos[1])):
            self.gameturn(self.g.get_rect_adress(event.pos[0], event.pos[1]))
