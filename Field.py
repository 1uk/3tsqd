import pygame
from pygame.locals import *
from C_Field import *

class Field(object):

    def __init__(self, x, y):
        #Status hot 0, won 1, full 2 see docs
        self._state = 0
        width = 200
        height = 200
        self.width = x * (width + 20)
        self.height = y * (height + 20)
        self.rect = pygame.Rect(self.width, self.height, width, height)

        self.on_init()

    def on_init(self):

        #Objekt Array
        self.cf = [[], [], []]
        for x in range(0, 3):
            for y in range(0, 3):
                self.cf[x].append(C_Field(x, y, self.rect))

    def draw(self):
        pass


    def bide(self):
        pass

