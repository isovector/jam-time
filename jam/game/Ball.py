import pygame

from jam.common.Vec3d import Vec3d, AXIS_VECTORS

import random
from Court import Court
from Entity import Entity
from Baller import Baller
from InputController import InputController
from MotionController import MotionController
from ActionController import ActionController

class BallState:
    default = 0
    shoot   = 1
    rebound = 2
    passed  = 3

class Ball(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos, 0.2, 0.2)
        self.capsule.ephemeral = True
        self.holder = None
        self.lastHolder = None
        self.motion = MotionController(self)
        self.state = BallState.default
        self.net = 0
        self.bounces = 0
        self.sinkPerc = 0

        def ballHandler(self, capsule):
            ball = self.owner
            if not ball.holder:
                player = capsule.owner
                if not isinstance(player, Baller):
                    return
                if ball.state == BallState.shoot and ball.lastHolder == player:
                    return

                ball.giveTo(player)

        self.capsule.onHit = ballHandler


    def giveTo(self, baller):
        self.holder = baller
        self.state = BallState.default
        self.motion.clear()

        baller.obtainBall()


    def release(self):
        self.lastHolder = self.holder
        self.holder = None


    def computeSinkage(self):
        # TODO: this is pretty shit
        stats = self.holder.stats
        self.sinkPerc = min(random.randrange(0, 100) + stats.shorts, 100)
        self.bounces = 0
        while random.random() < 0.8:
            self.bounces += 1
        self.bounces = min(self.bounces, 3)


    def shoot(self, shooter, net):
        netPos = Court.getNetPos(net)
        dir = netPos - self.pos
        dir.y = 0
        dir.length = 1

        dunkHeight = AXIS_VECTORS[1] * 3
        initialJump = self.pos + dunkHeight + AXIS_VECTORS[1] * netPos.y + dir
        controlPoint = netPos + dunkHeight + dir * 2

        self.net = net
        self.state = BallState.shoot
        self.computeSinkage()

        self.release()
        self.motion.moveAlongPath([initialJump, controlPoint, netPos], 1)
        self.motion.afterMoveDo(lambda x: self.onContact())


    def doBounce(self):
        self.motion.moveToPosition(Court.getNetPos(self.net), 0.2)
        self.motion.afterMoveDo(lambda x: self.onContact())


    def onContact(self):
        self.state = BallState.rebound
        if self.sinkPerc < 15:
            # HUGE REBOUND
            pass

        if self.bounces != 0:
            self.bounces -= 1
            self.motion.moveToPosition(Court.getNetPos(self.net) + AXIS_VECTORS[1], 0.2)
            self.motion.afterMoveDo(lambda x: self.doBounce())
            return

        if random.randrange(0, 100) < self.sinkPerc:
            self.game.goal(self.net)

        self.motion.moveToPosition(Court.getGroundPos(self.net), 0.5)
        self.state = BallState.default


    def draw(self, canvas, screenPos, scale):
        width = 20. * scale
        height = 20. * scale

        shadowPos = self.game.camera.toScreen(Vec3d(self.pos.x, 0, self.pos.z))
        shadowWidth = 20. * scale
        shadowHeight = 20. * scale

        pygame.draw.ellipse(canvas, 0x000000, (shadowPos[0] - shadowWidth / 2, shadowPos[1] - shadowHeight / 2, shadowWidth, shadowHeight))
        pygame.draw.ellipse(canvas, 0xFF8800, (screenPos[0] - width / 2, screenPos[1] - height, width, height))


    def update(self, delta):
        if self.holder:
            self.capsule.teleport(self.holder.pos + AXIS_VECTORS[1] * 0.5)
        else:
            self.motion.update(delta)
