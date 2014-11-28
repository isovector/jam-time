from jam.common.Vec3d import Vec3d
from jam.framework.Application import Application

from Court import Court
import Constants

from pygame.locals import *
nameToKey = {"Up":K_w, "Down":K_s, "Left":K_a, "Right":K_d, "Shoot":K_e, "Pass":K_f, "Turbo":K_LSHIFT}

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 7.
        self.isEnabled = True

    def enable(self, value):
        self.isEnabled = value

    def update(self, delta):
        if not self.isEnabled:
            return

        motion = self.owner.motion
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

        if Application.keymap[nameToKey["Shoot"]]:
            if turbo and dir.x * self.owner.net > 0:
                self.owner.action.dunk()
            else:
                self.owner.action.shoot()

        if Application.keymap[nameToKey["Pass"]]:
            self.owner.action.passing()

        motion.move(dir * delta * self.speed)

    def onInputEvent(self, event):
        pass
