from jam.common.Vec3d import Vec3d
from jam.framework.Application import Application

from pygame.locals import *

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 1.25
    
    def update(self, delta):
        motion = self.owner.motion
        dir = Vec3d(0, 0, 0)
        
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
        pass
