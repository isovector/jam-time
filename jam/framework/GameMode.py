class GameMode:
    def __init__(self):
        pass
        
    def init(self):
        pass
        
    def update(self, delta):
        print("update is not defined in GameMode")
        
    def draw(self, canvas):
        print("draw is not defined in GameMode")
    
    def onInputEvent(self, event):
        print("Input event: valid controller input")