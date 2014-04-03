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
            print "ende???"

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
        #mouseposition
        a = b = c = d = 0
        mx = event.pos[0]
        my = event.pos[1]
        #check in which rect mouse is in
        for a in range(0,3):
             for b in range(0,3):
                for c in range(0,3):
                    for d in range(0,3):
                        left = self.f[a][b].b[c][d].left
                        top = self.f[a][b].b[c][d].top
                        width = self.f[a][b].b[c][d].width
                        height = self.f[a][b].b[c][d].height

                        if (left <= mx and mx <= left + width):
                            x = a
                            xx = c
                        if (top <= my and my <= top + height):
                            y = b
                            yy = d
        if self.f[y][x].b[yy][xx].state == 0:
            self.f[y][x].b[yy][xx].state = player
            print player
            self.turn += 1
        #print "turn += 1"
        #print "Geklickt:", x, "-", y, "-", xx, "-" ,yy

