#!/usr/bin/python2

import sys,math

sys.dont_write_bytecode = 1

import pygame
from pygame.locals import *

class EventHandler:
    def eventFilter(self, event):
        pygame.init()
        controllerInput = [K_w, K_d, K_e]
        quitInput = [K_ESCAPE, K_q]
        
        if event.type == QUIT or (event.type == KEYDOWN and (event.key in quitInput)):
            return "QUIT"
        elif (event.type == KEYDOWN and (event.key in controllerInput)):
            return "CONTROLLER"
                     
    def __init__ (self, event):
        self.event = event
        self.type = self.eventFilter(event)