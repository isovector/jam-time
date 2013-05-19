from Baller import Baller
from jam.framework.GameMode import GameMode

class JamMode(GameMode):
    def __init__(self):
        GameMode.__init__(self)
        self.baller = Baller()
        
    def init(self):
        print("Initialized Jamming")
        
    def update(self, delta):
        pass
        
    def draw(self, canvas):
        pass
        