from jam.common.Vec3d import Vec3d
from jam.framework.Application import Application
import Queue


from pygame.locals import *
nameToKey = {"Up":K_w, "Down":K_s, "Left":K_a, "Right":K_d, "Shoot":K_e, "Pass":K_f, "Turbo":K_t}

class InputController:
    def __init__(self, owner):
        self.owner = owner
        self.speed = 1.25
        self.actionQ = Queue.Queue()
        self.frameCounter = 0
    
    def update(self, delta):
        motion = self.owner.motion
        dir = Vec3d(0, 0, 0)
        
        if self.frameCounter == 6:
            #Collect all items in the queue, find combination and send to onIE
            self.frameCounter = 0
        else:
            self.frameCounter = self.frameCounter + 1
        
        if Application.keymap[nameToKey["Up"]]:
            dir.z = 1
        if Application.keymap[nameToKey["Down"]]:
            dir.z = -1
        if Application.keymap[nameToKey["Left"]]:
            dir.x = -1
        if Application.keymap[nameToKey["Right"]]:
            dir.x = 1
        if Application.keymap[nameToKey["Shoot"]]:
            self.actionQ.put("Shoot")
        if Application.keymap[nameToKey["Pass"]]:
            self.actionQ.put("Pass")
        if Application.keymap[nameToKey["Turbo"]]:
            self.actionQ.put("Turbo")
        
        motion.move(dir * delta * self.speed)
        
    def onInputEvent(self, event):
        pass
