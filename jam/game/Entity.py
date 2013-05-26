from jam.common.Vec3d import Vec3d

from Capsule import Capsule

class Entity:
    def __init__(self, pos):
        self.capsule = Capsule(pos, 0.5, 2)
        
    def update(self, delta):
        pass
        
    def draw(self, canvas, screenPos, scale):
        pass
        
    @property
    def pos(self):
        return self.capsule.pos