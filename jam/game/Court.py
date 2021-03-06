import pygame

import Constants
from jam.common.Vec3d import Vec3d, AXIS_VECTORS
from Basket import Basket

class Court:
    LENGTH = 28
    GFX_LENGTH = 1800
    DEPTH = 15
    GFX_DEPTH = 300
    BASKET_OFFSET = 1.575
    BASKET_HEIGHT = 3.04
    BOARD_WIDTH = 1.8
    BOARD_HEIGHT = 1.05
    RUNOFF = 2
    LONG_RADIUS = 7.24

    def __init__(self):
        width = Court.LENGTH / 2
        depth = Court.DEPTH / 2
        self.topLeft = Vec3d(-width, 0, -depth)
        self.botLeft = Vec3d(-width, 0, +depth)
        self.topRight = Vec3d(+width, 0, -depth)
        self.botRight = Vec3d(+width, 0, +depth)

        self.baskets = [ Basket(-1), Basket(1) ]

    def draw(self, camera, canvas):
        pygame.draw.polygon(canvas, 0xFFAA77, (camera.toScreen(self.topLeft),
                                                camera.toScreen(self.topRight),
                                                camera.toScreen(self.botRight),
                                                camera.toScreen(self.botLeft)))
        for basket in self.baskets:
            basket.draw(camera, canvas)


    @staticmethod
    def getGroundPos(net):
        return Vec3d(
            (Court.LENGTH / 2 - Court.BASKET_OFFSET) * net,
            0,
            0)

    @staticmethod
    def getNetPos(net):
        return Court.getGroundPos(net) + Court.BASKET_HEIGHT * AXIS_VECTORS[1]

    @staticmethod
    def getBounds():
        width = Court.LENGTH / 2
        depth = Court.DEPTH / 2
        return (-width, width, 0, 100, -depth, depth)

