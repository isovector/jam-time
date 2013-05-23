import pygame

from Entity import Entity
from InputController import InputController
from MotionController import MotionController
from ActionController import ActionController

class Baller(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos)
        self.input = InputController(self)
        self.motion = MotionController(self)
        self.action = ActionController(self)
        
    def draw(self, canvas, screenPos, scale):
        width = 50. * scale
        height = 100. * scale
        pygame.draw.rect(canvas, 0xFF0000, (screenPos[0] - width / 2, screenPos[1] - height, width, height))
        
    def update(self, delta):
        self.input.update(delta)
        self.motion.update(delta)