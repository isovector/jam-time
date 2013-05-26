class MotionController:
    def __init__(self, owner):
        self.owner = owner
    
    def update(self, delta):
        pass
        
    def move(self, relative):
        self.owner.capsule.move(relative)
