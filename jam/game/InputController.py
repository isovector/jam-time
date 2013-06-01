from jam.common.Vec3d import Vec3d
from jam.framework.Application import Application

import Constants

from pygame.locals import *
nameToKey = {"Up":K_w, "Down":K_s, "Left":K_a, "Right":K_d, "Shoot":K_e, "Pass":K_f, "Turbo":K_t}

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 7.
    
    def update(self, delta):
        motion = self.owner.motion
        dir = Vec3d(0, 0, 0)
        
        if Application.keymap[nameToKey["Up"]]:
            dir.z = 1
        if Application.keymap[nameToKey["Down"]]:
            dir.z = -1
        if Application.keymap[nameToKey["Left"]]:
            dir.x = -1
        if Application.keymap[nameToKey["Right"]]:
            dir.x = 1
        if Application.keymap[nameToKey["Shoot"]]:
            self.owner.action.dunk(Vec3d(-Constants.COURT_LENGTH / 2 + Constants.BASKET_OFFSET, Constants.BASKET_HEIGHT, 0))
            
        if Application.keymap[nameToKey["Pass"]]:
            self.owner.action.passing()
        
        motion.move(dir * delta * self.speed)
        
    def onInputEvent(self, event):
        pass
