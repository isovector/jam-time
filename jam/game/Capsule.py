from jam.common.Vec3d import Vec3d

class Capsule:
    def __init__(self, pos, radius, height):
        self.pos = pos
        self.radius = radius
        self.height = height
        self.manager = 0
        
    def register(self, manager):
        self.manager = manager
        
    def move(self, rel):
        self.manager.moveCapsule(self, rel, [])
        
    @property
    def x(self):
        return self.pos.x
        
    @property
    def y(self):
        return self.pos.y
        
    @property
    def z(self):
        return self.pos.z