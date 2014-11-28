from pygame.locals import *

from jam.common.Vec3d import Vec3d, AXIS_VECTORS
from Court import Court

class ActionController:
    def __init__(self, owner):
        self.owner = owner

    def passing(self):
        ball = self.owner.game.ball
        if self.owner.hasBall:
            ball.capsule.teleport(Vec3d(0, 0, 0))
            ball.release()

    def jump(self):
        self.owner.jump()

    def shoot(self):
        if self.owner.hasBall:
            dist = (self.owner.pos - Court.getGroundPos(self.owner.net)).get_length()

            self.owner.game.ball.shoot(self.owner, self.owner.net, dist)

    def dunk(self):
        if not self.owner.hasBall:
            return

        netPos = Court.getNetPos(self.owner.net)
        dir = netPos - self.owner.pos
        dir.y = 0
        dir.length = 1

        dunkHeight = AXIS_VECTORS[1] * self._getDunkHeight()
        initialJump = self.owner.pos + dunkHeight + AXIS_VECTORS[1] * netPos.y + dir
        controlPoint = netPos + dunkHeight + dir * 2

        self.owner.input.enable(False)
        self.owner.motion.moveAlongPath([initialJump, controlPoint, netPos], 0.7)

        def nextAction(baller):
            baller.motion.moveToPosition(Court.getGroundPos(baller.net), 0.5)
            baller.motion.afterMoveDo(lambda baller: baller.input.enable(True))
        self.owner.motion.afterMoveDo(nextAction)


    def _getDunkHeight(self):
        return 3


    def onInputAction(self, action):
        pass

