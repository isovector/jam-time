from InputController import InputController
from Ball import BallState
from Court import Court
from jam.common.Vec3d import Vec3d

class AIController(InputController):
    def __init__(self, owner):
        InputController.__init__(self, owner)
        self.turn = 0

    def update(self, delta):
        baller = self.owner
        ball = baller.game.ball

        ballDir = ball.pos - baller.pos
        netDir = Court.getGroundPos(baller.net) - baller.pos
        self.turn += 1

        if self.turn % 3 == 0:
            return

        if not baller.hasBall:
            if ball.state == BallState.shoot:
                baller.action.move(delta, -netDir, True)
            else:
                baller.action.move(delta, ballDir, False)
        else:
            if netDir.length < Court.LONG_RADIUS:
                baller.action.shoot()
            else:
                baller.action.move(delta, netDir, False)

