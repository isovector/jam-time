from Entity import Entity

class Baller(Entity):
    def __init__(self):
        Entity.__init__(self)
        print("Baller initialized")