import pygame
from pygame.locals import *
from Boxes import *

import time

class Fields(object):

    #static variables
    width = 200
    height = 200
    gap = 20

    def __init__(self, x, y):
        #Status hot 0, won 1, full 2 see docs
        self._state = 0
        self.left = x * (width + gap)
        self.top = y * (height + gap)
        self.rect = pygame.Rect(self.left, self.top, width, height)
        #instantinating boxes
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


    def bide(self):
        pass

    def render(self, window):
        for x in range(0,3):
            for y in range(0,3):
                self.b[x][y].fill(window)

