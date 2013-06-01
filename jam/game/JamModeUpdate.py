from jam.common.Vec3d import Vec3d

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)
        
        self.totalTime += delta
            
        self.camera.focus = self.player.pos
        
        #for entity in self.entities:
        self.player.update(delta)