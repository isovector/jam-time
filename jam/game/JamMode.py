from Camera import Camera
from Baller import Baller
from Court import Court

import pygame
from jam.common.Vec3d import Vec3d
from jam.framework.GameMode import GameMode

class JamMode(GameMode):
    def __init__(self):
        GameMode.__init__(self)
        
        self.camera = Camera((700,400), (), 10, 100)
        self.court = Court()
        self.entities = []
        
        self.totalTime = 0
        
        
    def init(self):
        self.entities.append(Baller(Vec3d(-14, 0, -7)))
        #self.entities.append(Baller(Vec3d(600, 0, 300)))
        #self.entities.append(Baller())
        
        #self.camera.focus = Vec3d(-14, 0, 0)
        
        print("Initialized Jamming")
        
        
    def update(self, delta):
        self.camera.update(delta)
        
        self.totalTime += delta
        
        if 5 < self.totalTime < 10:
            self.entities[0].pos += Vec3d(5, 0, 2) * delta
            
        self.camera.focus = self.entities[0].pos
        
        #self.entities[1].pos += Vec3d(0, 0, 5) * delta
        #self.entities[2].pos += Vec3d(0, 0, 100.) * delta
        
        for entity in self.entities:
            entity.update(delta)
        
        
    def draw(self, canvas):
        self.court.draw(self.camera, canvas)
        for entity in self.entities:
            entity.draw(canvas, self.camera.toScreen(entity.pos), self.camera.getDepthModifier(entity.pos))
        