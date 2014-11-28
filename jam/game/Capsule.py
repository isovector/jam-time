from jam.common.Vec3d import Vec3d

class Capsule:
    def __init__(self, owner, pos, radius, height):
        self.owner = owner
        self.pos = pos
        self.radius = radius
        self.height = height
        self.manager = 0
        self.ephemeral = False
        self.onHit = None

    def register(self, manager):
        self.manager = manager

    def teleport(self, pos):
        self.pos = pos

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
