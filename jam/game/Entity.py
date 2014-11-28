from jam.common.Vec3d import Vec3d

from Capsule import Capsule

class Entity:
    def __init__(self, pos, radius, height):
        self.capsule = Capsule(self, pos, radius, height)
        self.game = None

    def update(self, delta):
        pass

    def register(self, game):
        self.game = game

    def draw(self, canvas, screenPos, scale):
        pass

    @property
    def pos(self):
        return self.capsule.pos
