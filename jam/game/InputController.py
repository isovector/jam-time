from jam.common.Vec3d import Vec3d
from jam.game.ContextController import ContextController
from jam.framework.Application import Application

from pygame.locals import *
  

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 1.25
        self.actionBuffer = None
        self.frameCounter = 0
        self.context = ContextController() 
    
    def update(self, delta):
        motion = self.owner.motion
        dir = Vec3d(0, 0, 0)
        
        if self.frameCounter >= 6:
            self.context.sendPress(self.actionBuffer)
            self.actionBuffer = None
            self.frameCounter = 0
        elif self.actionBuffer != None:
            self.frameCounter = self.frameCounter + 1
            
        if Application.keymap[K_w]:
            dir.z = 1
        if Application.keymap[K_s]:
            dir.z = -1
        if Application.keymap[K_a]:
            dir.x = -1
        if Application.keymap[K_d]:
            dir.x = 1

        motion.move(dir * delta * self.speed)
        
    def onInputEvent(self, event):
        if (self.actionBuffer == None) and (event.type == KEYDOWN):
            self.actionBuffer = event.key
        elif (event.type == KEYUP) and(event.key == self.actionBuffer):
            self.context.sendTap(self.actionBuffer)
            self.actionBuffer = None
        elif (event.type == KEYUP) and (event.key != self.actionBuffer):
            self.context.sendRelease(event.key)
        
            
            
