#!/usr/bin/python2

import sys,math

sys.dont_write_bytecode = 1

import pygame
from pygame.locals import *

class KeyMap:
    def __init__ (self):
        self.keymap = {K_a:False, K_b: False, K_c: False, K_d: False, K_e: False, K_f: False, K_g: False, K_h: False, K_i: False, K_j: False, K_k: False, K_l: False, K_m: False, 
                       K_n:False, K_o: False, K_p: False, K_q: False, K_r: False, K_s: False, K_t: False, K_u: False, K_v: False, K_w: False, K_x: False, K_y: False, K_z: False} 
    
    def resetMap(self):
        self.keymap.clear()
        self.keymap = {K_a:False, K_b: False, K_c: False, K_d: False, K_e: False, K_f: False, K_g: False, K_h: False, K_i: False, K_j: False, K_k: False, K_l: False, K_m: False, 
                       K_n:False, K_o: False, K_p: False, K_q: False, K_r: False, K_s: False, K_t: False, K_u: False, K_v: False, K_w: False, K_x: False, K_y: False, K_z: False}
    def update(self, event):
            pygame.init()
            self.resetMap()
            self.keymap[event.key] = (event.type == KEYDOWN)


