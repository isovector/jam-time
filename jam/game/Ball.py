import pygame

from jam.common.Vec3d import Vec3d, AXIS_VECTORS

from Entity import Entity
from Baller import Baller
from InputController import InputController
from MotionController import MotionController
from ActionController import ActionController

def ballHandler(self, capsule):
    ball = self.owner
    if not ball.holder:
        player = capsule.owner
        if not isinstance(player, Baller):
            return
        ball.giveTo(player)


class Ball(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos, 0.2, 0.2)
        self.capsule.ephemeral = True
        self.capsule.onHit = ballHandler
        self.holder = None

    def giveTo(self, baller):
        self.holder = baller
        baller.obtainBall()

    def release(self):
        self.holder = None

    def draw(self, canvas, screenPos, scale):
        width = 50. * scale
        height = 100. * scale

        shadowPos = self.game.camera.toScreen(Vec3d(self.pos.x, self.pos.y, self.pos.z))
        shadowWidth = 20. * scale
        shadowHeight = 20. * scale

        pygame.draw.ellipse(canvas, 0xFF8800, (shadowPos[0] - shadowWidth / 2, shadowPos[1] - shadowHeight / 2, shadowWidth, shadowHeight))

    def update(self, delta):
        if self.holder:
            self.capsule.teleport(self.holder.pos + AXIS_VECTORS[1] * 0.5)
