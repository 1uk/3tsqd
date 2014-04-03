import pygame
from pygame.locals import *

import Fields

class Boxes(object):

    def __init__(self, x, y, prect):
        #Status Leer 0, Kreuz 1, Kreis 2
        self.state = 0
        self.width = 60
        self.height = 60
        self.left = prect.left + x * (self.width + 10)
        self.top = prect.top + y * (self.height + 10) 
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, 0xFFFFFF, self.rect, 0)

    def fill(self, window):
        #cross
        if (self.state == 1):
            gap = 10
            left = self.left + 10
            right = self.left + self.width - 10
            top = self.top + 10
            bottom = self.top + self.height - 10
            pygame.draw.line(window, 0x000000, (top, left), (bottom, right), 8)
            pygame.draw.line(window, 0x000000, (bottom, left), (top, right), 8)
        elif (self.state == 2):
            x = self.left + self.width/2
            y = self.top + self.height/2
            pygame.draw.circle(window, 0x000000, (y, x), 20)
            pygame.draw.circle(window, 0xFFFFFF, (y, x), 12)

    def on_init(self, coordinates):
        pass
