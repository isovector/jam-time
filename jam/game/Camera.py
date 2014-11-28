import math
import Constants
from Court import Court
from jam.common.Vec2d import Vec2d
from jam.common.Vec3d import Vec3d

class Camera:
    def __init__(self, viewPlane, bounds, fov, deadzone):
        self.viewPlane = viewPlane
        self.worldBounds = bounds
        self.fov = math.radians(fov)
        self.deadzone = deadzone
        self.farPlane = 50

        self.pos = Vec3d(0, 0, 0)
        self.focus = Vec3d(0, 0, 0)

        self.offset = (350, 200)
        self.depthMultiplier = Court.GFX_DEPTH / Court.DEPTH
        self.widthMultiplier = Court.GFX_LENGTH / Court.LENGTH

    def update(self, delta):
        pos = self.toScreen(self.pos)
        focus = self.toScreen(self.focus)

        if pos.get_distance(focus) > self.deadzone:
            self.pos -= (self.pos - self.focus) * delta * 2


    def getDepthModifier(self, world):
        return 1 / ((world.z - self.pos.z) / Court.DEPTH + 1.5)

    def toScreen(self, world):
        local = world - self.pos

        depthModifier = self.getDepthModifier(world)

        x = local.x * self.widthMultiplier * depthModifier
        y = local.z * self.depthMultiplier
        y += local.y * Constants.HEIGHT_SCALING * depthModifier

        return Vec2d(x + self.offset[0], -y + self.offset[1])
