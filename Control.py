import pygame
from pygame.locals import *

from Field import *

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
        self.f = [[], [], []]
        for x in range(0, 3):
            for y in range(0, 3):
                self.f[x].append(Field(x, y))

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

        self.on_cleanup()

    #Verarbeitet Spielerevent
    def on_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 0:
                self.on_lbutton_down(event)

    def on_lbutton_down(self, event):
        #get mouse coordinates
        x, y = pygame.mouse.get_pos()

        #check in which rect mouse is in
        #for x in range(0,3):
        #        #big x gap
        #        xcdt += x * 20
        #    for y in range(0,3):
        #        #big y gap
        #        ycdt += y *20
        #        for xx in range(0,3):
        #            #small x gap
        #            xxcdt += xx * 10
        #            for yy in range(0,3):
        #                #small y gap
        #                yycdt += yy * 10
        #                if ()

    #Spielroutine
    def on_loop(self):
        pass

    #Renderroutine
    def on_render(self):
        self.draw_rects()

    def draw_rects(self):
        #zeichnet alle grossen Felder
        for x in range(0, 3):
            for y in range(0, 3):
              #  pygame.draw.rect(self.window, 0xFFFFFF, self.f[x][y].rect, 0)
                for xx in range(0,3):
                    for yy in range(0,3):
                        pygame.draw.rect(self.window, 0x0000FF, self.f[x][y].cf[xx][yy].rect, 0)

        pygame.display.update()

    #Aufraeumen (nur ganz am Ende)
    def on_cleanup(self):
        pygame.quit()
