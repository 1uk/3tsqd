import pygame
from pygame.locals import *

from Field import *

#Steuerungsklasse
class Control(object):

    #Konstruktor
    def __init__(self):
        self.size = self.weight, self.height = 610, 610

    #Extra Initialisierungsfunktion
    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self._running = True

        #Objekt Array
        self.f = [[], [], []]
        for a in range(0, 3):
            for b in range(0, 3):
                self.f[a].append(Field(b, a))

    #Hauptfunktion (der Anfang & das Ende)
    def on_execute(self):
        #fuehrt on_init() aus und prueft fehler
        if (self.on_init() == False):
            self._running = False

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
        pass

    #Spielroutine
    def on_loop(self):
        pass

    #Renderroutine
    def on_render(self):
        #zeichnet alle grossen Felder
        for a in range(0, 3):
            for b in range(0, 3):
                pygame.draw.rect(self.window, 0xFFFFFF, self.f[a][b].rect, 0)
                for c in range(0,3):
                    for d in range(0,3):
                        pygame.draw.rect(self.window, 0x0000FF, self.f[a][b].cf[c][d].rect, 0)

        pygame.display.update()

    #Aufraeumen (nur ganz am Ende)
    def on_cleanup(self):
        pygame.quit()
