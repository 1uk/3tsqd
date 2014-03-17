import pygame
from pygame.locals import *

import Field

class C_Field(object):

    def __init__(self, x, y):
        #Status Leer 0, Kreuz 1, Kreis 2
        self.state = 0

        width = 60
        height = 60
        self.rect = pygame.Rect(x* (width + 10), y*(height + 10), width, height)

    def on_init(self, coordinates):
        pass
