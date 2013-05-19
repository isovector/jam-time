#!/usr/bin/python2

import sys,math
sys.dont_write_bytecode = 1

from jam.game.JamMode import JamMode
from jam.framework.Application import Application
from jam.framework.GameMode import GameMode


jam = JamMode()
jam.init()
gameMode = GameMode()
app = Application(gameMode)
app.init(gameMode) 

while True:
    jam.update(0.1)
    jam.draw(0)
    app.setMode(gameMode)
    app.setupWindow()
    app.runGame()