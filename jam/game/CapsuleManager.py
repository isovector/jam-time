from jam.common.Vec2d import Vec2d
from jam.common.Vec3d import Vec3d

def inVerticalConstraint(capsule, other):
    return capsule.y < other.y < capsule.y + capsule.height
            or other.y < capsule.y < other.y + other.height


class CapsuleManager:
    def __init__(self):
        self.capsules = []
    
    def addCapsule(self, capsule):
        capsule.register(self)
        self.capsules.append(capsule)
        
    def moveCapsule(self, capsule, rel):
        desired = capsule.pos + rel
        desired2d = Vec2d(desired.x, desired.z)
        
        for other in self.capsules:
            if capsule == other:
                continue
            
            other2d = Vec2d(other.pos.x, other.pos.z)
            if desired2d.get_distance(other2d) > capsule.radius + other.radius:
                continue
                
            if not inVerticalConstraint(capsule, other):
                continue
            
            #TODO(sandy): this should actually figure out the direction
            # and split the force
            rel = rel * 0.5
            self.moveCapsule(other, rel)
        
        capsule.pos += rel