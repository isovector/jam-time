from jam.common.Vec3d import Vec3d
from Ball import BallState

class JamModeUpdate:
    def update(self, delta):
        self.camera.update(delta)

        self.totalTime += delta

        if self.ball.state != BallState.default:
            self.camera.focus = self.ball.pos
        else:
            self.camera.focus = self.player.pos

        for entity in self.entities:
            entity.update(delta)
