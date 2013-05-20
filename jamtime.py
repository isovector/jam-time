#!/usr/bin/python2

import sys,math
sys.dont_write_bytecode = 1

from jam.game.JamMode import JamMode
from jam.framework.Application import Application

jam = JamMode()
jam.init()

app = Application(jam)
app.setMode(jam)
app.setupWindow()
app.runGame()
