from Baller import Baller
from Ball import Ball
from Camera import Camera
from Capsule import Capsule
from CapsuleManager import CapsuleManager
from Court import Court
from JamModeUpdate import JamModeUpdate

import pygame
from jam.common.Vec3d import Vec3d
from jam.framework.GameMode import GameMode

class JamMode(JamModeUpdate, GameMode):
    def __init__(self):
        GameMode.__init__(self)

        self.camera = Camera((700,400), (), 10, 100)
        self.court = Court()
        self.entities = []

        self.physics = CapsuleManager(Court.getBounds())
        self.totalTime = 0
        self.font = pygame.font.SysFont(None, 36)
        self.score = [0, 0]


    def init(self):

        self.player = self.addEntity(Baller(Vec3d(0, 0, 0)))
        self.ball = self.addEntity(Ball(Vec3d(0, 0, 0)))


    def goal(self, net, points):
        self.score[(net + 1) / 2] += points


    def addEntity(self, entity):
        self.physics.addCapsule(entity.capsule)
        self.entities.append(entity)
        entity.register(self)
        return entity


    def draw(self, canvas):
        self.court.draw(self.camera, canvas)

        self.entities = sorted(self.entities, key=lambda entity: -entity.pos.z)
        for entity in self.entities:
            entity.draw(canvas, self.camera.toScreen(entity.pos), self.camera.getDepthModifier(entity.pos))

        text = self.font.render("%d:%d" % (self.score[1], self.score[0]), False, (0, 0, 0))
        canvas.blit(text, (340, 15))

