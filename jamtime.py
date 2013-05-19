#!/usr/bin/python2

import sys,math
sys.dont_write_bytecode = 1

from jam.game.JamMode import JamMode

jam = JamMode()
jam.init()

while True:
    jam.update(0.1)
    jam.draw(0)