import pygame
from jam.common.Vec3d import Vec3d, AXIS_VECTORS

class Basket:
    def __init__(self, net):
        from Court import Court

        netPos = Court.getNetPos(net) + Vec3d(0.5, 0, 0) * net
        self.netBaseBot = Vec3d(net * (Court.LENGTH / 2 + 2 * Court.BASKET_OFFSET), 0, 0)
        self.netBaseTop = netPos
        self.net = Court.getNetPos(net)
        self.netBoardBotLeft = netPos + Vec3d(0, 0, Court.BOARD_WIDTH / 2)
        self.netBoardBotRight = netPos + Vec3d(0, 0, -Court.BOARD_WIDTH / 2)
        self.netBoardTopLeft = netPos + Vec3d(0, Court.BOARD_HEIGHT, Court.BOARD_WIDTH / 2)
        self.netBoardTopRight = netPos + Vec3d(0, Court.BOARD_HEIGHT, -Court.BOARD_WIDTH / 2)

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

        net = camera.toScreen(self.net)
        pygame.draw.ellipse(canvas, 0xFF0000, (net[0] - netWidth / 2, net[1] - netHeight / 2, netWidth, netHeight), 3)

