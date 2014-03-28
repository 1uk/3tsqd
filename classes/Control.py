import pygame
from pygame.locals import *
from Fields import *

import time

#Steuerungsklasse
class Control(object):

    #Konstruktor
    def __init__(self):
        self.size = self.weight, self.height = 640, 640

    #Extra Initialisierungsfunktion
    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self._running = True

        #Objekt Array
        self.init_field()

    #Hauptfunktion (der Anfang & das Ende)
    def on_execute(self):
        #fuehrt on_init() aus und prueft fehler
        if (self.on_init() == False):
            self._running = False

        self.on_render()
        #Laeuft von Anfang bis Objektende
        while (self._running):
            #Bei events wie Mausklick
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
                self.on_lbutton_down(event)


    #Spielroutine
    def on_loop(self):
        pass


    #Renderroutine
    def on_render(self):
        pygame.display.update()

    def init_field(self):
        self.f = [[], [], []]
        for y in range(0, 3):
            for x in range(0, 3):
                self.f[x].append(Fields(x, y))
                self.f[x][y].draw(self.window)

    #Aufraeumen (nur ganz am Ende)
    def on_cleanup(self):
        pygame.quit()






    def on_lbutton_down(self, event):
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
        self.f[y][x].b[yy][xx].fill(1, self.window)
        print "Geklickt:", x, "-", y, "-", xx, "-" ,yy

