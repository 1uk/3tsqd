import pygame
from pygame.locals import *

import Field

class C_Field(object):

    def __init__(self, x, y, prect):
        #Status Leer 0, Kreuz 1, Kreis 2
        self.state = 0
        width = 60
        height = 60
        self.width = prect.left + x * (width + 10)
        self.height = prect.top + y * (height + 10) 
        self.rect = pygame.Rect(self.width, self.height, width, height)

    def on_init(self, coordinates):
        pass
