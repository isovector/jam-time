from pygame.locals import *

from jam.common.Vec3d import Vec3d, AXIS_VECTORS

class ActionController:
    def __init__(self, owner):
        self.owner = owner
    
    def passing(self):
        pass
        
    def shoot(self):
        pass
    
    def dunk(self, netPos):
        dir = netPos - self.owner.pos
        dir.y = 0
        dir.length = 1
        
        dunkHeight = AXIS_VECTORS[1] * self._getDunkHeight()
        initialJump = self.owner.pos + dunkHeight + AXIS_VECTORS[1] * netPos.y + dir
        controlPoint = netPos + dunkHeight + dir * 2
        
        netFloor = Vec3d(netPos)
        netFloor.y = 0
        
        self.owner.motion.moveAlongPath([initialJump, controlPoint, netPos], 0.7)
        self.owner.motion.afterMoveDo(lambda baller: baller.motion.moveToPosition(netFloor, 0.5))
        
        
    def _getDunkHeight(self):
        return 3
        
        
    def onInputAction(self, action):
        pass
    