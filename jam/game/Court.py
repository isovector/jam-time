import pygame

import Constants
from jam.common.Vec3d import Vec3d

from PsychedelicController import PsychedelicController

class Court:
    def __init__(self):
        width = Constants.COURT_LENGTH / 2
        depth = Constants.COURT_DEPTH / 2
        self.topLeft = Vec3d(-width, 0, -depth)
        self.botLeft = Vec3d(-width, 0, +depth)
        self.topRight = Vec3d(+width, 0, -depth)
        self.botRight = Vec3d(+width, 0, +depth)
        self.psychedelics = PsychedelicController()
        
    def update(self, delta):
        self.psychedelics.update(delta)
        
    def draw(self, camera, canvas):
        pygame.draw.polygon(canvas, self.psychedelics.getColor(), (camera.toScreen(self.topLeft),
                                                camera.toScreen(self.topRight),
                                                camera.toScreen(self.botRight),
                                                camera.toScreen(self.botLeft)))