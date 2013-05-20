#!/usr/bin/python2

import sys,math

sys.dont_write_bytecode = 1

import pygame
from pygame.locals import *
from pygame.color import *

from GameMode import *

class Application:
    def __init__(self, gameMode):
        self.gameMode = gameMode
        self.width = 700
        self.height = 400
        self.fps = 60
        self.delta = 1/self.fps
        self.clock = None
        self.screen = None
        
    def setMode(self, newMode):
        self.gameMode = newMode
    
    def setupWindow(self):        
        #Initialize Pygame
        pygame.init()
    
        #Setup the window
        pygame.display.set_caption('Jam Time') 
        self.screen = pygame.display.set_mode((self.width, self.height))        
        self.clock = pygame.time.Clock() 
    
    def runGame(self):
        running = True
        
        while running:
            self.screen.fill(pygame.color.THECOLORS["blue"])
        
            for event in pygame.event.get():  
                if event.type == QUIT or (event.type == KEYDOWN and (event.key in [K_ESCAPE, K_q])):        
                    running = False         
            
            self.gameMode.update(self.delta);
            self.gameMode.draw(self.screen);
            pygame.display.flip()



