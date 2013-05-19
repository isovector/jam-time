from jam.common.Vec3d import Vec3d

class Entity:
    def __init__(self, pos):
        print("Entity initialized")
        self.pos = pos
        
    def update(self, delta):
        pass
        
    def draw(self, camera, canvas):
        pass