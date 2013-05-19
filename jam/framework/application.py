#!/usr/bin/python2

import sys,math

sys.dont_write_bytecode = 1

import pygame
from pygame.locals import *
from pygame.color import *

#-------------------------------------

width, height = 700, 400
fps = 60
dt = 1./fps

#-------------------------------------

def main():
	#Initialize Pygame
	pygame.init()
	
	#Setup the window
	pygame.display.set_caption('Jam Time') 
	screen = pygame.display.set_mode((width, height))
	
	clock = pygame.time.Clock()
	running = True
	
	while running:
		screen.fill(pygame.color.THECOLORS["blue"])
		
		for event in pygame.event.get():  
			if event.type == QUIT or (event.type == KEYDOWN and (event.key in [K_ESCAPE, K_q])):        
				running = False         
			
		pygame.display.flip()
		clock.tick(fps)
		
		
if __name__ == '__main__':
	sys.exit(main())