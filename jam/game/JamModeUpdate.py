from jam.common.Vec3d import Vec3d

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)
        
        self.totalTime += delta
            
        self.camera.focus = self.player.pos
        
        if 20 < self.totalTime < 21:
            self.player.motion.moveToPosition(Vec3d(0,0,0))
            self.totalTime = 21
        if 34 < self.totalTime:
            self.player.motion.moveAlongPath([Vec3d(-3, 6, 0), Vec3d(6, 6, 0), Vec3d(10, 0, 0)])
            self.totalTime = 0
        
        #for entity in self.entities:
        self.player.update(delta)