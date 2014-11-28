from jam.common.Vec3d import Vec3d
from jam.framework.Application import Application

from Court import Court
import Constants

from pygame.locals import *
nameToKey = {"Up":K_w, "Down":K_s, "Left":K_a, "Right":K_d, "Shoot":K_e, "Pass":K_f, "Turbo":K_LSHIFT}

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 7 + (owner.stats.speed - 5) / 2.
        self.isEnabled = True
        self.isJumping = False

    def enable(self, value):
        self.isEnabled = value

    def update(self, delta):
        baller = self.owner

        motion = baller.motion
        dir = Vec3d(0, 0, 0)
        turbo = False

        if Application.keymap[nameToKey["Up"]]:
            dir.z = 1
        if Application.keymap[nameToKey["Down"]]:
            dir.z = -1
        if Application.keymap[nameToKey["Left"]]:
            dir.x = -1
        if Application.keymap[nameToKey["Right"]]:
            dir.x = 1
        if Application.keymap[nameToKey["Turbo"]]:
            dir *= 2
            # TODO: decrease turbo timer
            # scale speed by character's speed
            turbo = True

        velocity = dir * self.speed

        if Application.keymap[nameToKey["Shoot"]]:
            if not self.isEnabled:
                return

            if turbo and dir.x * baller.net > 0:
                baller.action.dunk()
            elif not self.isJumping:
                self.isJumping = True
                baller.action.jump(velocity)
        elif self.isJumping:
            if baller.motion.isMoving:
                baller.action.shoot()
            self.isJumping = False

        if not self.isEnabled:
            return


        if Application.keymap[nameToKey["Pass"]]:
            baller.action.passing()

        motion.move(velocity * delta)

    def onInputEvent(self, event):
        pass
