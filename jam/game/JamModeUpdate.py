from jam.common.Vec3d import Vec3d

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)
        
        self.totalTime += delta
            
        self.camera.focus = self.entities[0].pos
        
        #for entity in self.entities:
        self.entities[0].update(delta)