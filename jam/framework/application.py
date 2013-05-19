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
		
	def setMode(self, newMode):
		self.gameMode = newMode
		pass
	
	def setupWindow(self):
		width, height = 700, 400
		
		#Initialize Pygame
		pygame.init()
	
		#Setup the window
		pygame.display.set_caption('Jam Time') 
		screen = pygame.display.set_mode((width, height))		
	
	def runGame(self):
		running = True
		
		while running:
		screen.fill(pygame.color.THECOLORS["blue"])
		
		for event in pygame.event.get():  
			if event.type == QUIT or (event.type == KEYDOWN and (event.key in [K_ESCAPE, K_q])):        
				running = False         
			
		pygame.display.flip()



