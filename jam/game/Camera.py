class Camera:
    def __init__(self, viewPlane):
        self.viewPlane = viewPlane
        
    def update(self, delta):
        pass

    def toScreen(self, world):
        x = world.x
        y = world.z / z + world.y
        return (x,y), 1.0 - world.z/20