import random

import pygame
from pygame.math import Vector2

import core


class Creep2:
    def __init__(self):
        self.pos = Vector2(random.randint (0,800),random.randint (0,800))
        self.taille = 5
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.masse = 10

    def show (self):
        core.Draw.circle(self.color,[int(self.pos.x),int(self.pos.y)],self.taille)







