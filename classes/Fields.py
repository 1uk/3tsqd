import pygame
from pygame.locals import *
from Boxes import *

import time

class Fields(object):

    #static variables
    size = w, h = 640,640
    width = 200
    height = 200
    gap = 20

    def __init__(self, x, y):
        #Status hot 0, won 1, full 2 see docs
        print self.gap
        self._state = 0
        self.left = x * (self.width + self.gap)
        self.top = y * (self.height + self.gap)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
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
                self.b[x][y].render(window)

