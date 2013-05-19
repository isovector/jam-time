from Camera import Camera
from Baller import Baller

from jam.common.Vec3d import Vec3d
from jam.framework.GameMode import GameMode

class JamMode(GameMode):
    def __init__(self):
        GameMode.__init__(self)
        
        self.camera = Camera((700,400))
        self.entities = []
        
        
    def init(self):
        self.entities.append(Baller(Vec3d(0, 0, 0)))
        self.entities.append(Baller(Vec3d(100, 0, 100)))
        self.entities.append(Baller(Vec3d(200, 0, 200)))
        #self.entities.append(Baller())
        
        print("Initialized Jamming")
        
        
    def update(self, delta):
        self.camera.update(delta)
        
        self.entities[0].pos += Vec3d(10, 0, 0) * delta
        self.entities[1].pos += Vec3d(0, 10, 0) * delta
        self.entities[2].pos += Vec3d(0, 0, 10) * delta
        
        for entity in self.entities:
            entity.update(delta)
        
        
    def draw(self, canvas):
        for entity in self.entities:
            entity.draw(self.camera, canvas)
        