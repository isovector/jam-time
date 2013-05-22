from jam.common.Vec3d import Vec3d

class Entity:
    def __init__(self, pos):
        self.pos = pos
        
    def update(self, delta):
        pass
        
    def draw(self, canvas, screenPos, scale):
        pass