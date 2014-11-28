import pygame
import math
from jam.common.Vec3d import Vec3d, AXIS_VECTORS

class Basket:
    def __init__(self, net):
        from Court import Court

        self.net = net

        netPos = Court.getNetPos(net) + Vec3d(0.5, 0, 0) * net
        self.netBaseBot = Vec3d(net * (Court.LENGTH / 2 + 2 * Court.BASKET_OFFSET), 0, 0)
        self.netBaseTop = netPos
        self.netPos = Court.getNetPos(net)
        self.netBoardBotLeft = netPos + Vec3d(0, 0, Court.BOARD_WIDTH / 2)
        self.netBoardBotRight = netPos + Vec3d(0, 0, -Court.BOARD_WIDTH / 2)
        self.netBoardTopLeft = netPos + Vec3d(0, Court.BOARD_HEIGHT, Court.BOARD_WIDTH / 2)
        self.netBoardTopRight = netPos + Vec3d(0, Court.BOARD_HEIGHT, -Court.BOARD_WIDTH / 2)

        ground = Court.getGroundPos(net)
        self.longTopLeft = ground - Court.LONG_RADIUS * (AXIS_VECTORS[0] - AXIS_VECTORS[2])
        self.longBotRight = ground + Court.LONG_RADIUS * (AXIS_VECTORS[0] - AXIS_VECTORS[2])
        self.longTopLeft.z *= net
        self.longBotRight.z *= net


    def draw(self, camera, canvas):
        netWidth = 40
        netHeight = 20

        pygame.draw.line(canvas, 0x333333,
            camera.toScreen(self.netBaseBot),
            camera.toScreen(self.netBaseTop),
            5)

        pygame.draw.polygon(canvas, 0x222222,
            (camera.toScreen(self.netBoardTopLeft),
             camera.toScreen(self.netBoardTopRight),
             camera.toScreen(self.netBoardBotRight),
             camera.toScreen(self.netBoardBotLeft)))

        net = camera.toScreen(self.netPos)
        pygame.draw.ellipse(canvas, 0xFF0000, (net[0] - netWidth / 2, net[1] - netHeight / 2, netWidth, netHeight), 3)

        longTL = camera.toScreen(self.longTopLeft)
        longBR = camera.toScreen(self.longBotRight)

        x = min(longTL[0], longBR[0])
        y = min(longTL[1], longBR[1])
        w = abs(longTL[0] - longBR[0])
        h = abs(longTL[1] - longBR[1])

        if int(min(w, h)) > 1:
            start = math.pi / 2
            end = math.pi / 2 * 3
            if self.net == -1:
                start = -math.pi / 2
                end = math.pi / 2
            pygame.draw.arc(canvas, 0xFF0000, (x, y, w, h), start, end, 1)

