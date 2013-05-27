from Baller import Baller
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
        
        self.physics = CapsuleManager()
        self.totalTime = 0
        
        
    def init(self):
        self.addBaller(Baller(Vec3d(-14, 0, -7)))
        self.addBaller(Baller(Vec3d(8, 0, 0)))
        self.addBaller(Baller(Vec3d(8, 0, -1)))
        self.addBaller(Baller(Vec3d(9, 0, -0.5)))
        
        self.addBaller(Baller(Vec3d(-7, 1, -5)))
        
        # THIS IS A BIG OLD HACK
        self.player = self.entities[0]
        
    
    def addBaller(self, baller):
        self.physics.addCapsule(baller.capsule)
        self.entities.append(baller)
        baller.register(self)
        
        
    def draw(self, canvas):
        self.court.draw(self.camera, canvas)
        
        self.entities = sorted(self.entities, key=lambda entity: -entity.pos.z)
        for entity in self.entities:
            entity.draw(canvas, self.camera.toScreen(entity.pos), self.camera.getDepthModifier(entity.pos))
        