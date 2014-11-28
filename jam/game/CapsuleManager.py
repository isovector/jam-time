from jam.common.Vec2d import Vec2d
from jam.common.Vec3d import Vec3d

def inVerticalConstraint(capsule, other):
    return capsule.y < other.y < capsule.y + capsule.height or \
            other.y < capsule.y < other.y + other.height or \
            capsule.y == other.y


class CapsuleManager:
    def __init__(self):
        self.capsules = []

    def addCapsule(self, capsule):
        capsule.register(self)
        self.capsules.append(capsule)

    def moveCapsule(self, capsule, rel, ignore):
        desired = capsule.pos + rel
        desired2d = Vec2d(desired.x, desired.z)

        slowCount = 0

        if not capsule.ephemeral:
            hit = []
            for other in self.capsules:
                if capsule == other or other in ignore:
                    continue

                other2d = Vec2d(other.pos.x, other.pos.z)
                if desired2d.get_distance(other2d) > capsule.radius + other.radius:
                    continue

                if inVerticalConstraint(capsule, other):
                    hit.append(other)
                    if not other.ephemeral:
                        slowCount += 1

            if slowCount != 0:
                rel *= 1. / (slowCount + 1)
            magnitude = rel.length

        capsule.pos += rel
        if not capsule.ephemeral:
            ignore.append(capsule)
            for other in hit:
                if capsule.onHit:
                    capsule.onHit(capsule, other)
                if other.onHit:
                    other.onHit(other, capsule)
                if not other.ephemeral:
                    dir = other.pos - capsule.pos
                    dir.length = magnitude
                    self.moveCapsule(other, dir, ignore)
