import pygame

import Constants
from jam.common.Vec3d import Vec3d, AXIS_VECTORS

class Court:
    LENGTH = 28
    GFX_LENGTH = 1400
    DEPTH = 15
    GFX_DEPTH = 300
    BASKET_OFFSET = 1.575
    BASKET_HEIGHT = 3.04
    RUNOFF = 2

    def __init__(self):
        width = Court.LENGTH / 2
        depth = Court.DEPTH / 2
        self.topLeft = Vec3d(-width, 0, -depth)
        self.botLeft = Vec3d(-width, 0, +depth)
        self.topRight = Vec3d(+width, 0, -depth)
        self.botRight = Vec3d(+width, 0, +depth)

    def draw(self, camera, canvas):
        pygame.draw.polygon(canvas, 0xFFAA77, (camera.toScreen(self.topLeft),
                                                camera.toScreen(self.topRight),
                                                camera.toScreen(self.botRight),
                                                camera.toScreen(self.botLeft)))

    @staticmethod
    def getGroundPos(net):
        return Vec3d(
            (Court.LENGTH / 2 - Court.BASKET_OFFSET) * net,
            0,
            0)

    @staticmethod
    def getNetPos(net):
        return Court.getGroundPos(net) + Court.BASKET_HEIGHT * AXIS_VECTORS[1]

