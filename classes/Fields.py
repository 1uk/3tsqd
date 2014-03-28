import pygame
from pygame.locals import *
from Boxes import *

import time

class Fields(object):

    def __init__(self, x, y):
        #Status hot 0, won 1, full 2 see docs
        self._state = 0
        width = 200
        height = 200
        self.left = x * (width + 20)
        self.top = y * (height + 20)
        self.rect = pygame.Rect(self.left, self.top, width, height)
        self.init_boxes()

    def init_boxes(self):
        self.b = [[], [], []]
        for x in range(0, 3):
            for y in range(0, 3):
                self.b[x].append(Boxes(x, y, self.rect))


    def draw(self, window):
        for x in range(0,3):
            for y in range(0,3):
                self.b[x][y].draw(window)
                pygame.display.update()


    def bide(self):
        pass

