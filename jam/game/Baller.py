import pygame
from Entity import Entity

class Baller(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos)
        
    def draw(self, camera, canvas):
        pos, size = camera.toScreen(self.pos)
        pygame.draw.rect(canvas, 0xFF0000, (pos[0], pos[1], 25 * size, 25 * size))