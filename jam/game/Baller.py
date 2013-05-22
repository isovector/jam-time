import pygame
from Entity import Entity

class Baller(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos)
        
    def draw(self, canvas, screenPos, scale):
        width = 50. * scale
        height = 100. * scale
        pygame.draw.rect(canvas, 0xFF0000, (screenPos[0] - width / 2, screenPos[1] - height, width, height))