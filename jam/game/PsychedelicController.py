import math

class PsychedelicController:
    def __init__(self):
        self.time = 0
        
    def update(self, delta):
        self.time += delta
        
    def getColor(self, phase = 0):
        red = self.wave(2, phase, 128) + 127
        green = self.wave(5, phase, 128) + 127
        blue = self.wave(7, phase, 128) + 127
       
        return (int(red) << 16) | (int(green) << 8) | int(blue)
        
    def wave(self, freq, phase, mag):
        return mag * math.cos(freq * self.time + phase)