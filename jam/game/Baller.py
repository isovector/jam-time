from Entity import Entity

class Baller(Entity):
    def __init__(self, pos):
        Entity.__init__(self, pos)
        print("Baller initialized")
        
    def draw(self, camera, canvas):
        pass