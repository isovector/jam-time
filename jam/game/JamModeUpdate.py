from jam.common.Vec3d import Vec3d

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)
        
        self.totalTime += delta
            
        self.camera.focus = self.entities[0].pos
        
        #self.entities[1].pos += Vec3d(0, 0, 5) * delta
        #self.entities[2].pos += Vec3d(0, 0, 100.) * delta
        
        for entity in self.entities:
            entity.update(delta)