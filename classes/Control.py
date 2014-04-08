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
            #self.on_render()

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
        #clicked field
        cf = self.g.f[a][b]

        if cf.bide:
            #clicked box
            cb = cf.b[c][d]
            #current player
            cp = self.p[self.turn%2].p_id + 1

            #fill empty box with current player
            if (cb.state == 0):
                cb.state = cp

            #if field is not won yet, set winner
            if cf.state == 0:
                winner = cf.is_won(c, d)
                cf.state = winner
                #checke is the game is won
                gamewinner = self.g.is_won(a, b)
                if gamewinner:
                    print "Player", gamewinner, "has won!"

            #after first turn
            if self.turn == 0:
                for a in range(3):
                    for b in range(3):
                        self.g.f[a][b].bide = False

            cf.bide = False
            self.g.f[c][d].bide = True
            self.on_render()

            self.turn += 1
            self.player = self.turn % 2 + 1




    ############
    ## Events ##
    ############
    #siehe pygame.org/docs/ref/event.html
    #------------------------------------

    def on_lbutton_down(self, event):
        #if a box is clicked
        if (self.g.get_rect_adress(event.pos[0], event.pos[1])):
            self.gameturn(self.g.get_rect_adress(event.pos[0], event.pos[1]))
