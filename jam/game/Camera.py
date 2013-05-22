import math
import Constants
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
        self.depthMultiplier = Constants.COURT_GFX_DEPTH / Constants.COURT_DEPTH
        self.widthMultiplier = Constants.COURT_GFX_LENGTH / Constants.COURT_LENGTH
        
    def update(self, delta):
        pass
        
    def getDepthModifier(self, world):
        return 1 / ((world.z - self.focus.z) / Constants.COURT_DEPTH + 1.5)

    def toScreen(self, world):
        local = world - self.focus
        
        depthModifier = self.getDepthModifier(world)
        
        x = local.x * self.widthMultiplier * depthModifier
        y = local.z * self.depthMultiplier + local.y

        return (x + self.offset[0], -y + self.offset[1])