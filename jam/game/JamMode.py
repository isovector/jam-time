from Camera import Camera
from Baller import Baller
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
        
        self.totalTime = 0
        
        
    def init(self):
        self.entities.append(Baller(Vec3d(-14, 0, -7)))
        #self.entities.append(Baller(Vec3d(600, 0, 300)))
        #self.entities.append(Baller())
        
        #self.camera.focus = Vec3d(-14, 0, 0)
        
        print("Initialized Jamming")
        
        
    def draw(self, canvas):
        self.court.draw(self.camera, canvas)
        for entity in self.entities:
            entity.draw(canvas, self.camera.toScreen(entity.pos), self.camera.getDepthModifier(entity.pos))
        