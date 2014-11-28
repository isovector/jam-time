from jam.common.Vec3d import Vec3d
from Ball import BallState

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)

        self.totalTime += delta

        self.camera.focus = self.ball.pos

        for entity in self.entities:
            entity.update(delta)
