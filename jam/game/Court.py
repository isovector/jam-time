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
    BOARD_WIDTH = 1.8
    BOARD_HEIGHT = 1.05
    RUNOFF = 2

    def __init__(self):
        width = Court.LENGTH / 2
        depth = Court.DEPTH / 2
        self.topLeft = Vec3d(-width, 0, -depth)
        self.botLeft = Vec3d(-width, 0, +depth)
        self.topRight = Vec3d(+width, 0, -depth)
        self.botRight = Vec3d(+width, 0, +depth)

        netPos = Court.getNetPos(-1) - Vec3d(0.5, 0, 0)
        self.leftNetBaseBot = Vec3d(-width - 2 * Court.BASKET_OFFSET, 0, 0)
        self.leftNetBaseTop = netPos
        self.leftNet = Court.getNetPos(-1)
        self.leftNetBoardBotLeft = netPos + Vec3d(0, 0, Court.BOARD_WIDTH / 2)
        self.leftNetBoardBotRight = netPos + Vec3d(0, 0, -Court.BOARD_WIDTH / 2)
        self.leftNetBoardTopLeft = netPos + Vec3d(0, Court.BOARD_HEIGHT, Court.BOARD_WIDTH / 2)
        self.leftNetBoardTopRight = netPos + Vec3d(0, Court.BOARD_HEIGHT, -Court.BOARD_WIDTH / 2)

        netPos = Court.getNetPos(1) + Vec3d(0.5, 0, 0)
        self.rightNetBaseBot = Vec3d(width + 2 * Court.BASKET_OFFSET, 0, 0)
        self.rightNetBaseTop = netPos
        self.rightNet = Court.getNetPos(1)
        self.rightNetBoardBotright = netPos + Vec3d(0, 0, Court.BOARD_WIDTH / 2)
        self.rightNetBoardBotRight = netPos + Vec3d(0, 0, -Court.BOARD_WIDTH / 2)
        self.rightNetBoardTopright = netPos + Vec3d(0, Court.BOARD_HEIGHT, Court.BOARD_WIDTH / 2)
        self.rightNetBoardTopRight = netPos + Vec3d(0, Court.BOARD_HEIGHT, -Court.BOARD_WIDTH / 2)

    def draw(self, camera, canvas):
        pygame.draw.polygon(canvas, 0xFFAA77, (camera.toScreen(self.topLeft),
                                                camera.toScreen(self.topRight),
                                                camera.toScreen(self.botRight),
                                                camera.toScreen(self.botLeft)))
        netWidth = 40
        netHeight = 20

        pygame.draw.line(canvas, 0x333333,
            camera.toScreen(self.leftNetBaseBot),
            camera.toScreen(self.leftNetBaseTop),
            5)
        pygame.draw.polygon(canvas, 0x222222,
            (camera.toScreen(self.leftNetBoardTopLeft),
             camera.toScreen(self.leftNetBoardTopRight),
             camera.toScreen(self.leftNetBoardBotRight),
             camera.toScreen(self.leftNetBoardBotLeft)))
        leftNet = camera.toScreen(self.leftNet)
        pygame.draw.ellipse(canvas, 0xFF0000, (leftNet[0] - netWidth / 2, leftNet[1] - netHeight / 2, netWidth, netHeight), 3)

        pygame.draw.line(canvas, 0x333333,
            camera.toScreen(self.rightNetBaseBot),
            camera.toScreen(self.rightNetBaseTop),
            5)
        pygame.draw.polygon(canvas, 0x222222,
            (camera.toScreen(self.rightNetBoardTopright),
             camera.toScreen(self.rightNetBoardTopRight),
             camera.toScreen(self.rightNetBoardBotRight),
             camera.toScreen(self.rightNetBoardBotright)))
        rightNet = camera.toScreen(self.rightNet)
        pygame.draw.ellipse(canvas, 0xFF0000, (rightNet[0] - netWidth / 2, rightNet[1] - netHeight / 2, netWidth, netHeight), 3)

    @staticmethod
    def getGroundPos(net):
        return Vec3d(
            (Court.LENGTH / 2 - Court.BASKET_OFFSET) * net,
            0,
            0)

    @staticmethod
    def getNetPos(net):
        return Court.getGroundPos(net) + Court.BASKET_HEIGHT * AXIS_VECTORS[1]

