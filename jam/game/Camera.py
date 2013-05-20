import math
from jam.common.Vec3d import Vec3d

class Camera:
    def __init__(self, viewPlane, bounds, fov, deadzone):
        self.viewPlane = viewPlane
        self.worldBounds = bounds
        self.fov = math.radians(fov)
        self.deadzone = deadzone
        self.farPlane = 50
        self.focus = Vec3d(0, 0, 0)
        self.offset = (350, 200)
        
    def update(self, delta):
        pass

    def toScreen(self, world):
        local = world - self.focus
        
        scaleFactor = 1 - 2 * math.tan(self.fov) * (local.z / 50)

        x = local.x * scaleFactor
        y = (local.y) * scaleFactor

        return (x + self.offset[0], -y + self.offset[1]), scaleFactor