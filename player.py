import random

import pygame
from pygame.math import Vector2



class player:
    def __init__(self):
        self.pos = Vector2(random.randint(800, 800))
        self.taille = 50
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.masse = 50
        self.Vmax = 60
        self.Acc = 20
        self.Vmin = 10

    def move (self,screen):

        posX, posY = pygame.mouse.get_pos()




    def canEat(self, creep):
        if self.creep.pos == self.player.pos:
            self.player.taille == + 1
            self.creep.taille == - 10




        pygame.draw.circle(self.taille, self.color, self.pos , int(self.masse))




