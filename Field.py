import pygame
from pygame.locals import *
from C_Field import *

class Field(object):

    def __init__(self, x, y):
        #Status hot 0, won 1, full 2 see docs
        self._state = 0
        width = 200
        height = 200
        self.rect = pygame.Rect(x* (width + 5), y*(height + 5), width, height)

        self.on_init()

    def on_init(self):

        #Objekt Array
        self.cf = [[], [], []]
        for a in range(0, 3):
            for b in range(0, 3):
                self.cf[a].append(C_Field(b, a))


    def bide(self):
        pass

