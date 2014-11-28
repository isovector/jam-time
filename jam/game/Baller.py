import pygame

from jam.common.Vec3d import Vec3d, AXIS_VECTORS

from Entity import Entity
from Stats import Stats
from InputController import InputController
from MotionController import MotionController
from ActionController import ActionController

class Baller(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos, 0.5, 2)
        self.stats = Stats()
        self.input = InputController(self)
        self.motion = MotionController(self)
        self.action = ActionController(self)
        self.color = 0xAA0077
        self.net = -1

    def land(self, pos):
        def onGround(baller):
            # TODO: traveling
            baller.input.enable(True)
            baller.capsule.pos.y = 0

        self.motion.moveToPosition(pos, 0.5)
        self.motion.afterMoveDo(onGround)


    def jump(self, velocity):
        self.input.enable(False)

        pos = Vec3d(self.pos + velocity)
        duration = 0.5
        self.motion.moveToPosition(
            self.pos + AXIS_VECTORS[1] * self._getJumpHeight() + velocity * duration,
            duration)
        self.motion.afterMoveDo(lambda baller: self.land(pos))

    def _getJumpHeight(self):
        return 1.5


    def obtainBall(self):
        pass

    @property
    def hasBall(self):
        return self.game.ball.holder == self

    def draw(self, canvas, screenPos, scale):
        width = 50. * scale
        height = 100. * scale

        if not (0 < screenPos[0] < 700 and 0 < screenPos[1] < 400):
            screenPos.clamp((15, 685, 15, 400))
            width = 30
            height = 30
            pygame.draw.ellipse(canvas, self.color, (screenPos[0] - width / 2, screenPos[1] - height, width, height), 5)
            return


        shadowPos = self.game.camera.toScreen(Vec3d(self.pos.x, 0, self.pos.z))
        shadowWidth = 80. * scale
        shadowHeight = 30. * scale

        pygame.draw.ellipse(canvas, 0x000000, (shadowPos[0] - shadowWidth / 2, shadowPos[1] - shadowHeight / 2, shadowWidth, shadowHeight))
        pygame.draw.rect(canvas, self.color, (screenPos[0] - width / 2, screenPos[1] - height, width, height))

    def update(self, delta):
        self.input.update(delta)
        self.motion.update(delta)
